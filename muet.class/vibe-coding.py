# ──────────────────────────────────────────────────────────────
#  STUDENT PERFORMANCE TRACKER
#  Console-only | No imports | Pure Python built-ins
# ──────────────────────────────────────────────────────────────

# --- Nested dictionary: each student holds marks, attendance, assignments ---
students = {
    "Ali": {
        "marks":      [78, 85, 90, 72, 88],
        "attendance": 82,
        "assignment": 75,
    },
    "Sara": {
        "marks":      [92, 95, 88, 97, 91],
        "attendance": 96,
        "assignment": 94,
    },
    "Usman": {
        "marks":      [45, 50, 38, 55, 42],
        "attendance": 60,
        "assignment": 48,
    },
    "Fatima": {
        "marks":      [65, 70, 68, 74, 60],
        "attendance": 78,
        "assignment": 72,
    },
    "Hassan": {
        "marks":      [30, "absent", 45, None, 28],   # edge-case: bad values
        "attendance": "N/A",                           # edge-case: string
        "assignment": None,                            # edge-case: missing
    },
}

SUBJECTS = ["Math", "English", "Science", "Computer", "Physics"]


# --- Safely extract a numeric value; return None if invalid ---
def safe_num(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    return None


# --- Calculate average from a list, skipping invalid entries ---
def calculate_average_marks(marks_list):
    if not isinstance(marks_list, list) or len(marks_list) == 0:
        return None
    valid = [safe_num(m) for m in marks_list]
    valid = [v for v in valid if v is not None]
    if len(valid) == 0:
        return None
    return sum(valid) / len(valid)


# --- Determine performance grade from avg, attendance, assignment ---
def evaluate_performance(avg, attendance, assignment):
    # Validate all three inputs
    avg_ok  = safe_num(avg)
    att_ok  = safe_num(attendance)
    asgn_ok = safe_num(assignment)

    if avg_ok is None or att_ok is None or asgn_ok is None:
        return "Cannot Evaluate (incomplete data)"

    if avg_ok >= 80 and att_ok >= 75 and asgn_ok >= 70:
        return "Excellent"
    elif avg_ok >= 65 and att_ok >= 75 and asgn_ok >= 70:
        return "Good"
    elif avg_ok >= 50 and att_ok >= 60 and asgn_ok >= 50:
        return "Average"
    else:
        return "Poor"


# --- Format a single mark value for display ---
def fmt_mark(value):
    n = safe_num(value)
    return f"{n}" if n is not None else "N/A"


# --- Format a percentage value for display ---
def fmt_pct(value):
    n = safe_num(value)
    return f"{n}%" if n is not None else "N/A"


# ──────────────────────────────────────────────────────────────
#  MAIN REPORT
# ──────────────────────────────────────────────────────────────
print("=" * 58)
print("         STUDENT PERFORMANCE TRACKER REPORT")
print("=" * 58)

for name, info in students.items():

    # Safely fetch each field with a fallback
    marks      = info.get("marks",      [])
    attendance = info.get("attendance", None)
    assignment = info.get("assignment", None)

    # Compute average and grade
    avg   = calculate_average_marks(marks)
    grade = evaluate_performance(avg, attendance, assignment)

    # Student header
    print(f"\n  Student : {name}")
    print(f"  {'-' * 46}")

    # Subject-wise marks
    print(f"  {'Subject':<12} {'Marks':>8}")
    print(f"  {'-' * 22}")
    for i, subject in enumerate(SUBJECTS):
        mark = marks[i] if i < len(marks) else "Missing"
        print(f"  {subject:<12} {fmt_mark(mark):>8}")

    # Summary block
    print(f"  {'-' * 30}")
    avg_display = f"{avg:.2f}" if avg is not None else "N/A"
    print(f"  {'Average Marks:':<22} {avg_display:>8}")
    print(f"  {'Attendance:':<22} {fmt_pct(attendance):>8}")
    print(f"  {'Assignment Score:':<22} {fmt_pct(assignment):>8}")
    print(f"  {'-' * 30}")
    print(f"  {'Final Performance:':<22} {grade:>8}")

print("\n" + "=" * 58)
print("  SUMMARY")
print("=" * 58)
print(f"  {'Name':<12} {'Avg':>6} {'Attend':>8} {'Assign':>8} {'Grade':>26}")
print("  " + "-" * 54)

for name, info in students.items():
    marks      = info.get("marks",      [])
    attendance = info.get("attendance", None)
    assignment = info.get("assignment", None)
    avg        = calculate_average_marks(marks)
    grade      = evaluate_performance(avg, attendance, assignment)

    avg_d  = f"{avg:.1f}" if avg is not None else "N/A"
    att_d  = fmt_pct(attendance)
    asgn_d = fmt_pct(assignment)
    print(f"  {name:<12} {avg_d:>6} {att_d:>8} {asgn_d:>8} {grade:>26}")

print("=" * 58)
