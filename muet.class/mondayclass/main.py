import pandas as pd

# csv file load

df = pd.read_csv("students.csv")

print("=== Student Data ===")
print(df)

# students average
df["Average"] = df[["Math", "Physics", "computer"]].mean(axis=1)

print("\n=== Average Marks ===")
print(df[["Name", "Average"]])

# greater average student

top_student_index = df["Average"].idxmax()
top_student = df.loc[top_student_index, "Name"]
top_average = df.loc[top_student_index, "Average"]

print(f"\n=== Highest Score ===")
print(f"Student: {top_student}, Average: [top_avg]")

print(f"\n=== Highest Scorer ===")
print(f"Student: {top_student}, Average: {top_avg}")

#  percentage calculate
df["Percentage"] = df["Average"]  # same value

# grade assign

def assign_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B" 
    else:
        return "C"
    
df["Grade"] = df["Percentage"].apply(assign_grade)

print("\n=== Final Result ===")
print(df[["Name", "Math", "Physics", "Computer", "Average", "Percentage", "Grade"]])
