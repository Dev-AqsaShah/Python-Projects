import base64
import json
import os
import shutil

import cv2
import numpy as np
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

DATASET_PATH = "dataset"
TRAINER_PATH = "trainer.yml"
LABELS_PATH = "labels.txt"
USERS_PATH = "users.json"
CONFIDENCE_THRESHOLD = 85  # LBPH mein kam confidence = behtar match

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def name_key(name):
    """Naam ko hamesha lowercase 'key' mein convert karta hai, taake folder/label/users.json
    teeno jaga naam ek jaisa match ho (case ke farq se bug na bane)."""
    return name.strip().lower()


def load_users():
    if not os.path.exists(USERS_PATH):
        return {}
    with open(USERS_PATH, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_PATH, "w") as f:
        json.dump(users, f, indent=2)


def load_labels():
    labels = {}
    if os.path.exists(LABELS_PATH):
        with open(LABELS_PATH, "r") as f:
            for line in f:
                id_, key = line.strip().split(",")
                labels[int(id_)] = key
    return labels


def decode_image(data_url):
    header, encoded = data_url.split(",", 1)
    img_bytes = base64.b64decode(encoded)
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_COLOR)


def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(120, 120))
    if len(faces) == 0:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    face_img = gray[y:y + h, x:x + w]
    face_img = cv2.resize(face_img, (200, 200))
    face_img = cv2.equalizeHist(face_img)  # lighting ka farq kam karne ke liye
    return face_img


def predict_face(face_img):
    """Returns (key, confidence) ya (None, None) agar koi trained model na ho."""
    if not os.path.exists(TRAINER_PATH):
        return None, None

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(TRAINER_PATH)
    labels = load_labels()

    id_, confidence = recognizer.predict(face_img)
    return labels.get(id_), confidence


def train_and_save():
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces = []
    labels = []
    label_ids = {}
    current_id = 0

    for key in os.listdir(DATASET_PATH):
        person_folder = os.path.join(DATASET_PATH, key)
        if not os.path.isdir(person_folder):
            continue

        if key not in label_ids:
            label_ids[key] = current_id
            current_id += 1

        for img_name in os.listdir(person_folder):
            img = cv2.imread(os.path.join(person_folder, img_name), cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(label_ids[key])

    if not faces:
        for path in (TRAINER_PATH, LABELS_PATH):
            if os.path.exists(path):
                os.remove(path)
        return

    recognizer.train(faces, np.array(labels))
    recognizer.save(TRAINER_PATH)

    with open(LABELS_PATH, "w") as f:
        for key, id_ in label_ids.items():
            f.write(f"{id_},{key}\n")


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/users")
def get_users():
    return jsonify(load_users())


@app.route("/api/users/<key>", methods=["DELETE"])
def delete_user(key):
    key = name_key(key)
    users = load_users()
    if key not in users:
        return jsonify({"error": "User not found"}), 404

    del users[key]
    save_users(users)

    person_folder = os.path.join(DATASET_PATH, key)
    if os.path.isdir(person_folder):
        shutil.rmtree(person_folder)

    train_and_save()
    return jsonify({"success": True})


@app.route("/api/register/check", methods=["POST"])
def register_check():
    """Capture shuru karne se pehle check: yeh naam ya yeh chehra already registered to nahi?"""
    data = request.json
    key = name_key(data.get("name", ""))
    users = load_users()

    if key in users:
        return jsonify({"duplicate": True, "reason": "name", "message": f"'{data.get('name')}' naam se koi pehle se registered hai."})

    face_img = detect_face(decode_image(data["image"]))
    if face_img is None:
        return jsonify({"duplicate": False, "no_face": True})

    matched_key, confidence = predict_face(face_img)
    if matched_key and confidence < CONFIDENCE_THRESHOLD and matched_key in users:
        matched_display = users[matched_key]["name"]
        return jsonify({"duplicate": True, "reason": "face", "message": f"Yeh chehra already '{matched_display}' ke naam se registered hai."})

    return jsonify({"duplicate": False})


@app.route("/api/register/capture", methods=["POST"])
def register_capture():
    data = request.json
    name = data.get("name", "").strip()
    if not name or "/" in name or "\\" in name:
        return jsonify({"error": "Invalid name"}), 400

    face_img = detect_face(decode_image(data["image"]))
    if face_img is None:
        return jsonify({"saved": False, "message": "No face detected"})

    key = name_key(name)
    person_folder = os.path.join(DATASET_PATH, key)
    os.makedirs(person_folder, exist_ok=True)
    existing = len(os.listdir(person_folder))
    cv2.imwrite(os.path.join(person_folder, f"{existing + 1}.jpg"), face_img)

    return jsonify({"saved": True, "count": existing + 1})


@app.route("/api/register/complete", methods=["POST"])
def register_complete():
    data = request.json
    name = data.get("name", "").strip()
    key = name_key(name)
    person_folder = os.path.join(DATASET_PATH, key)
    if not os.path.isdir(person_folder) or len(os.listdir(person_folder)) == 0:
        return jsonify({"error": "No photos captured for this user"}), 400

    train_and_save()

    users = load_users()
    users[key] = {
        "name": name,
        "roll_no": data.get("roll_no", ""),
        "department": data.get("department", ""),
        "trade": data.get("trade", ""),
    }
    save_users(users)

    return jsonify({"success": True})


@app.route("/api/recognize", methods=["POST"])
def recognize():
    if not os.path.exists(TRAINER_PATH):
        return jsonify({"status": "no_users"})

    face_img = detect_face(decode_image(request.json["image"]))
    if face_img is None:
        return jsonify({"status": "no_face"})

    key, confidence = predict_face(face_img)
    users = load_users()

    if key and confidence < CONFIDENCE_THRESHOLD and key in users:
        return jsonify({"status": "registered", "details": users[key]})

    return jsonify({"status": "unregistered"})


if __name__ == "__main__":
    app.run(debug=True, port=5051)
