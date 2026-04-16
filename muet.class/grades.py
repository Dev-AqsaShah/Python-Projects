# ask user to enter 5 student names and marks 
# save data to a file grades.txt, one student per line
# read back the file and print all records
# append a new students data without overwriting

with open("grades.txt", "w") as f:
    print("enter data for 5 students:\n")
    for i in range(1, 6):
        name = input(f"Student {i} name: ")
        marks = input(f"Student {i} marks: ")
        f.write(f"{name},{marks}\n")

print("\n--- read records ---\n")
with open("grades.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(f"Name: {name} | Marks: {marks}")

print("\n--- add new student data  (append) ---\n")
new_name = input("New student name: ")
new_marks = input("New student marks: ")

with open("grades.txt", "a") as f:
    f.write(f"{new_name},{new_marks}\n")

print("\n--- Updated records ---\n")
with open("grades.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(f"Name: {name} | Marks: {marks}")
