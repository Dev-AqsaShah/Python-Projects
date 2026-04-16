import os

all_files = os.listdir(".")

py_files = [f for f in all_files if f.endswith(".py")]

print("All files in current directory:")
for f in all_files:
    print(f"  {f}")

print("\n.py files only:")
for f in py_files:
    print(f"  {f}")
