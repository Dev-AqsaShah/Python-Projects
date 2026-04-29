# ══════════════════════════════════════════════════════════════
#  CHALLENGE 1 - Bug Hunt (20 pts)
#  Faulty Sensor Monitor - Karachi Factory Floor
# ══════════════════════════════════════════════════════════════

# ── TASK 1.1: Diagnose the Bugs ────────────────────────────────
#
#  BUG 1 (line: average = sum(readings) / len(readings)):
#    Jab readings list empty ho, len([]) = 0 hota hai.
#    Zero se divide karne par Python ZeroDivisionError crash karta hai.
#
#  BUG 2 (line: print(analyse_sensors(data_empty))):
#    data_empty = [] pass ki gayi, lekin function mein koi empty-list
#    check nahi tha — isliye BUG 1 trigger hota hai aur program band ho jata hai.
#
# ── TASK 1.2: AI Prompt Used ───────────────────────────────────
#
#  PROMPT:
#  "I have a Python function analyse_sensors(readings) that calculates
#   the average of a list and returns a status dict. It has two bugs:
#   Bug 1 - it crashes with ZeroDivisionError when the list is empty
#           because it does sum(readings)/len(readings) with no empty check.
#   Bug 2 - calling it with data_empty=[] triggers that crash.
#   Please fix the function so it handles an empty list gracefully and
#   returns {'average': 0, 'status': 'NO DATA'} instead of crashing."
#
# ── AI's Fixed Code ────────────────────────────────────────────

def analyse_sensors(readings):
    if not readings:                          # FIX: empty list handle karo
        return {'average': 0, 'status': 'NO DATA'}
    average = sum(readings) / len(readings)
    if average > 85:
        status = 'CRITICAL'
    elif average > 60:
        status = 'WARNING'
    else:
        status = 'OK'
    return {'average': round(average, 2), 'status': status}


# ── TASK 1.3: Verify - Run and Check Output ────────────────────

data_morning = [72, 68, 91, 55, 63]
data_empty   = []

print("=" * 50)
print("  CHALLENGE 1 - Sensor Bug Fix Output")
print("=" * 50)
print("data_morning :", analyse_sensors(data_morning))
print("data_empty   :", analyse_sensors(data_empty))
print("=" * 50)

# TASK 1.3 ANSWER:
# data_morning output: {'average': 69.8, 'status': 'WARNING'}
#   -> 69.8 > 60, isliye WARNING — factory ke liye sahi hai
#      (kuch sensors high readings de rahe hain, alert zaroori hai)
#
# data_empty output: {'average': 0, 'status': 'NO DATA'}
#   -> Ab crash nahi hota, clean message milta hai
#
# Status logic factory ke liye sahi hai:
#   > 85 = CRITICAL (danger zone, line band karo)
#   > 60 = WARNING  (supervisor ko batao)
#   <= 60 = OK      (sab theek)
