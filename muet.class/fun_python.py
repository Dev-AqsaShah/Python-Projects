# ==========================================
#   FUN PYTHON TASKS - MUET CLASS EDITION
# ==========================================

print("=" * 45)
print("   WELCOME TO FUN PYTHON CLASS!")
print("=" * 45)

# ------------------------------------------
# TASK 1: Roast My Name
# ------------------------------------------
print("\n--- TASK 1: Roast My Name ---")
name = input("Enter your name (if you dare): ")

if len(name) <= 3:
    print(f"Really {name}? Even variable names are longer than you!")
elif name.lower() == "sir" or name.lower() == "teacher":
    print(f"Oh {name}! You are already a genius... or at least you think so!")
elif len(name) > 8:
    print(f"{name}?! That name is so long, you'll get tired typing it in login forms!")
else:
    print(f"Hey {name}! Your coding future is bright... your electricity bill will be too!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 2: Pizza Bill Calculator
# ------------------------------------------
print("\n--- TASK 2: Pizza Bill ---")
pizzas = int(input("How many pizzas will you eat? (be honest): "))
price = 500
total = pizzas * price

print(f"\nTotal Bill: Rs. {total}")

if pizzas == 1:
    print("Only 1? Are you on a diet or just broke?")
elif pizzas <= 3:
    print("Okay... you seem like a reasonable human being.")
elif pizzas <= 6:
    print("WARNING: That many pizzas? Save your doctor's number first!")
else:
    print("DANGER! You are not eating pizza, pizza is eating YOU!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 3: Mood Detector
# ------------------------------------------
print("\n--- TASK 3: Mood Detector ---")
mood = input("What is your mood today? (happy/sad/bored/angry): ").lower()

if mood == "happy":
    print("Great! You must be the one whose code actually ran on the first try!")
elif mood == "sad":
    print("Don't be sad... even the best programmers cry over bugs!")
elif mood == "bored":
    print("Bored? Learn Python! Boredom and Python cannot exist together!")
elif mood == "angry":
    print("Angry? Did you review someone's code today?")
else:
    print(f"{mood}? That mood is not even in Python's dictionary!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 4: Pet Name Generator
# ------------------------------------------
print("\n--- TASK 4: Pet Name Generator ---")
color = input("Enter your favorite color: ")
animal = input("Enter your favorite animal: ")

pet_name = color.capitalize() + animal.capitalize() + "Jr"
print(f"\nYour funny pet name is: '{pet_name}'")
print(f"Now teach {pet_name} Python -- it will be a better coder than you!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 5: Simple Calculator (with Roast)
# ------------------------------------------
print("\n--- TASK 5: Funny Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
print(f"\n{num1} + {num2} = {total}")

if total == 0:
    print("Zero? Is that your bank balance too?")
elif total > 1000:
    print("Such a big number? Are you calculating a salary or a pizza bill?")
else:
    print("Good job! The calculator got it right. Whether YOU did is another story!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 6: Marks Feedback System
# ------------------------------------------
print("\n--- TASK 6: Marks Feedback ---")
marks = int(input("Enter your marks (no lying): "))

if marks > 100 or marks < 0:
    print("Those are not valid marks... stop breaking the calculator!")
elif marks >= 90:
    print("GENIUS ALERT! Skip class and apply to Google directly!")
elif marks >= 70:
    print("MashAllah! Above average... your parents will actually smile!")
elif marks >= 50:
    print("You passed! Sometimes that is all life asks for!")
elif marks >= 33:
    print("Barely passed! Take the back route home with your result card!")
else:
    print("Failed? No worries... even Python gives errors on the first run!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 7: Student vs Teacher Detector
# ------------------------------------------
print("\n--- TASK 7: Student vs Teacher ---")
role = input("What are you? (student/teacher): ").lower()

if role == "teacher":
    print("Oh! A teacher is here! Students thought you only existed to give marks!")
    print("Just kidding! You are the error handler of our lives!")
elif role == "student":
    print("Another surviving student! Is your assignment submitted or is your excuse ready?")
    print("Welcome to Python -- where errors become your best friends!")
else:
    print(f"{role}? That was not in the syllabus... go tell the teacher!")

input("\nPress Enter for next task...")

# ------------------------------------------
# TASK 8: Creative Challenge
# ------------------------------------------
print("\n--- TASK 8: Creative Challenge ---")
print("Your turn! Create any funny program using:")
print("  - input()")
print("  - if/else")
print("  - print()")
print("\nExample idea: Excuse Generator -- what to say when assignment is not done!")

excuse_needed = input("\nDo you need an excuse today? (yes/no): ").lower()

if excuse_needed == "yes":
    subject = input("What do you need an excuse for? ")
    print(f"\nPerfect excuse for '{subject}':")
    print("'Sir, my laptop was updating and Python deleted my file by itself!'")
    print("No money back guarantee on this excuse!")
else:
    print("Wow! An honest person! You are welcome in the Python community!")

# ------------------------------------------
# BONUS: Meme Champion
# ------------------------------------------
print("\n" + "=" * 45)
print("   BONUS: PYTHON MEME CHAMPION!")
print("=" * 45)
champ_name = input("\nEnter the name of the funniest programmer: ")
print(f"\nCongratulations {champ_name}!")
print(f"{champ_name} is now officially:")
print("***  PYTHON MEME CHAMPION  ***")
print("Certificate will be printed... when Python prints it itself!")
print("\n" + "=" * 45)
print("Class over! Go home and keep writing Python!")
print("=" * 45)
