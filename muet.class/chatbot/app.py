import os
import time

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

MAX_RETRIES = 3


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    response = None
    for attempt in range(MAX_RETRIES):
        response = requests.post(
            GEMINI_URL,
            json={"contents": [{"parts": [{"text": user_message}]}]},
        )
        if response.status_code != 503:
            break
        time.sleep(1.5 * (attempt + 1))

    if not response.ok:
        message = response.json().get("error", {}).get("message", "Request failed")
        if response.status_code == 503:
            message = "Gemini is busy right now, please try again in a moment."
        return jsonify({"error": message}), response.status_code

    data = response.json()
    reply = data["candidates"][0]["content"]["parts"][0]["text"]
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
