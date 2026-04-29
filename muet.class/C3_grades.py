# ══════════════════════════════════════════════════════════════
#  CHALLENGE 3 - Grade System Fix (20 pts)
#  University Results Processing - MUET Exam Office
# ══════════════════════════════════════════════════════════════

# ── TASK 3.1: Spot the Bug ─────────────────────────────────────
#
#  BUG: elif score > 50  (strict greater-than operator)
#
#  Explanation:
#    score = 50 ke liye condition check hoti hai: 50 > 50 = False
#    Isliye yeh elif skip ho jata hai aur else branch chalti hai jo 'F' return karta hai.
#    50 score wala student jo actually pass hai, use F grade mil raha tha — ye galat hai.
#
#  Correct operator: >= (greater than OR EQUAL TO)
#    50 >= 50 = True  ->  ab D (Pass) milega

# ── TASK 3.2: AI Prompt Used ───────────────────────────────────
#
#  PROMPT:
#  "Fix this Python grade function. It has a bug: score=50 gets grade F
#   because 'elif score > 50' uses strict >, but 50 is a passing mark.
#   Fix it to use >= 50.
#   Also add a dictionary called GRADE_DESCRIPTIONS with:
#     A+: Distinction, A: Excellent, B: Very Good, C: Good, D: Pass, F: Fail
#   Then print both the grade letter and description for each test score.
#   Also add input validation: raise ValueError if score is not 0-100."

# ── AI's Improved Code (Task 3.2) ─────────────────────────────

GRADE_DESCRIPTIONS = {
    'A+': 'Distinction',
    'A':  'Excellent',
    'B':  'Very Good',
    'C':  'Good',
    'D':  'Pass',
    'F':  'Fail',
}

def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise ValueError(f"Score must be a number, got: {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got: {score}")

    if score >= 90:
        letter = 'A+'
    elif score >= 80:
        letter = 'A'
    elif score >= 70:
        letter = 'B'
    elif score >= 60:
        letter = 'C'
    elif score >= 50:      # FIX: >= instead of >
        letter = 'D'
    else:
        letter = 'F'

    return letter, GRADE_DESCRIPTIONS[letter]


# ── Task 3.2 Output ───────────────────────────────────────────
print("=" * 50)
print("  CHALLENGE 3 - Grade System Output")
print("=" * 50)

test_scores = [95, 83, 71, 62, 50, 49, 0]
print(f"  {'Score':>6}  {'Grade':<4}  Description")
print("  " + "-" * 30)
for s in test_scores:
    letter, desc = assign_grade(s)
    print(f"  {s:>6}  {letter:<4}  {desc}")

# ── TASK 3.3: Edge Cases ──────────────────────────────────────
print("\n  Edge Case Tests (Task 3.3):")
print("  " + "-" * 40)
for edge in [50, 100, -5, 150]:
    try:
        letter, desc = assign_grade(edge)
        print(f"  score={edge:>4} -> {letter} ({desc})")
    except ValueError as e:
        print(f"  score={edge:>4} -> ERROR: {e}")

print("=" * 50)

# TASK 3.3 ANALYSIS:
#  score=50  -> D (Pass)    — BUG fix kaam kar raha hai
#  score=100 -> A+ (Distinction) — sahi hai
#  score=-5  -> ValueError  — invalid score, message clear hai
#  score=150 -> ValueError  — 100 se upar nahi ja sakta
#
#  Haan, function ko 0-100 range validate karni chahiye
#  kyunki exam marks is range se bahar nahi ho sakte.
#  Validation add ki gayi hai jo ValueError raise karta hai.
