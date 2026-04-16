import random

questions = [
    {"question": "Pakistan ka capital kya hai?", "answer": "islamabad"},
    {"question": "2 ki power 10 kitni hoti hai?", "answer": "1024"},
    {"question": "Python mein list banane ke liye konsa bracket use hota hai?", "answer": "[]"},
    {"question": "Is_prime(7) ka result kya hoga? (True/False)", "answer": "true"},
    {"question": "Circle ka area formula kya hai?", "answer": "pi*r*r"},
]

random.shuffle(questions)

score = 0

print("=== Welcome to Quiz Game ===\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    user_answer = input("Aapka jawab: ").strip().lower()
    if user_answer == q["answer"].lower():
        print("Sahi hai!\n")
        score += 1
    else:
        print(f"Galat! Sahi jawab: {q['answer']}\n")

print(f"=== Quiz Khatam! ===")
print(f"Aapka score: {score}/{len(questions)}")
