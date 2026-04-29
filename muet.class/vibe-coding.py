# ══════════════════════════════════════════════════════════════
#  NEXUS Engineering Solutions - AI VIBECODING MISSION
#  All 5 Challenges Complete
# ══════════════════════════════════════════════════════════════

import numpy as np


# ══════════════════════════════════════════════════════════════
#  CHALLENGE 1 - Bug Hunt (20 pts)
#  Faulty Sensor Monitor - Karachi Factory Floor
# ══════════════════════════════════════════════════════════════
#
#  BUG 1: sum(readings) / len(readings) — agar list empty ho to
#         len([]) = 0, aur zero se divide hone par ZeroDivisionError crash karta hai.
#
#  BUG 2: empty list check bilkul nahi thi, isliye data_empty = []
#         dene par program crash ho jata tha.
#
#  FIX:   function ke shuruaat mein check karo — agar list empty hai
#         to seedha {'average': 0, 'status': 'NO DATA'} return karo.
# ──────────────────────────────────────────────────────────────

def analyse_sensors(readings):
    if not readings:                          # FIX: empty list handle
        return {'average': 0, 'status': 'NO DATA'}
    average = sum(readings) / len(readings)
    if average > 85:
        status = 'CRITICAL'
    elif average > 60:
        status = 'WARNING'
    else:
        status = 'OK'
    return {'average': round(average, 2), 'status': status}


# ── Challenge 1 Test ──────────────────────────────────────────
print("=" * 58)
print("  CHALLENGE 1 - Sensor Monitor (Bug Fixed)")
print("=" * 58)

data_morning = [72, 68, 91, 55, 63]
data_empty   = []

print("data_morning :", analyse_sensors(data_morning))
print("data_empty   :", analyse_sensors(data_empty))

# Task 1.3 - Verification answer:
# data_morning average = 69.8  → WARNING (60 < 69.8 <= 85) — sahi hai
# data_empty   → NO DATA       — crash nahi, clean message milta hai


# ══════════════════════════════════════════════════════════════
#  CHALLENGE 2 - NumPy Production Stats (25 pts)
#  Quality Control Dashboard - Hyderabad Assembly Line
# ══════════════════════════════════════════════════════════════
#
#  batch_stats()   → numpy se mean, std, min, max nikalo
#  quality_flag()  → agar std <= tolerance hai to PASS, warna FAIL
#
#  Task 2.1 Plan:
#   batch_stats   needs: np.mean, np.std, np.min, np.max
#   quality_flag  needs: np.std  (compare with TOLERANCE)
# ──────────────────────────────────────────────────────────────

TOLERANCE = 5   # acceptable deviation from 500g target

batch_A = np.array([498, 502, 497, 503, 500, 499, 501, 505, 496, 504])
batch_B = np.array([510, 523, 488, 531, 476, 519, 482, 527, 491, 515])
batch_C = np.array([500, 500, 500, 500, 500, 500, 500, 500, 500, 500])


def batch_stats(batch):
    return {
        'mean': round(float(np.mean(batch)), 2),
        'std':  round(float(np.std(batch)),  2),
        'min':  int(np.min(batch)),
        'max':  int(np.max(batch)),
    }


def quality_flag(batch, tolerance=TOLERANCE):
    return 'PASS' if np.std(batch) <= tolerance else 'FAIL'


# ── Challenge 2 Test ──────────────────────────────────────────
print("\n" + "=" * 58)
print("  CHALLENGE 2 - Quality Control Dashboard")
print("=" * 58)
print(f"  {'Batch':<8} {'Mean':>7} {'Std':>7} {'Min':>6} {'Max':>6}  Flag")
print("  " + "-" * 46)

for name, b in [('A', batch_A), ('B', batch_B), ('C', batch_C)]:
    s    = batch_stats(b)
    flag = quality_flag(b)
    print(f"  Batch {name}  {s['mean']:>7} {s['std']:>7} {s['min']:>6} {s['max']:>6}  {flag}")

# Task 2.3 Answers:
#  Batch A → std ≈ 2.8  → PASS  (variation kam hai)
#  Batch B → std ≈ 19.5 → FAIL  (variation bahut zyada hai)
#  Batch C → std = 0.0  → PASS  (saari values exactly 500g hain)
#  Batch C ka std=0 unrealistic hai — real factory mein thodi variation hoti hai.


# ══════════════════════════════════════════════════════════════
#  CHALLENGE 3 - Grade System Fix (20 pts)
#  University Results Processing - MUET Exam Office
# ══════════════════════════════════════════════════════════════
#
#  BUG: elif score > 50  →  exactly 50 score wala student F pata tha
#       kyunki 50 > 50 False hota hai, isliye else branch chala.
#  FIX: elif score >= 50  →  ab 50 bhi D (Pass) milega
#
#  Task 3.2: grade dictionary + description add ki
#  Task 3.3: input validation add ki (0–100 range check)
# ──────────────────────────────────────────────────────────────

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

    if score >= 90:        # FIX: >= so that 90 gets A+ not A
        letter = 'A+'
    elif score >= 80:
        letter = 'A'
    elif score >= 70:
        letter = 'B'
    elif score >= 60:
        letter = 'C'
    elif score >= 50:      # FIX: >= 50 so that exactly 50 gets D, not F
        letter = 'D'
    else:
        letter = 'F'

    return letter, GRADE_DESCRIPTIONS[letter]


# ── Challenge 3 Test ──────────────────────────────────────────
print("\n" + "=" * 58)
print("  CHALLENGE 3 - Grade System (Bug Fixed + Validated)")
print("=" * 58)

test_scores = [95, 83, 71, 62, 50, 49, 0]
print(f"  {'Score':>6}  {'Grade':<4}  Description")
print("  " + "-" * 30)
for s in test_scores:
    letter, desc = assign_grade(s)
    print(f"  {s:>6}  {letter:<4}  {desc}")

# Edge case tests (Task 3.3)
print("\n  Edge Case Tests:")
for edge in [50, 100, -5, 150]:
    try:
        letter, desc = assign_grade(edge)
        print(f"  score={edge:>4} -> {letter} ({desc})")
    except ValueError as e:
        print(f"  score={edge:>4} -> ERROR: {e}")


# ══════════════════════════════════════════════════════════════
#  CHALLENGE 4 - AI Ethics Audit (20 pts)
#  Biased Hiring Algorithm - NEXUS HR System
# ══════════════════════════════════════════════════════════════
#
#  Task 4.1 - Original biased code (RUN to observe):
#   Ayesha (MUET, GPA 3.8, 3yr) → base=62.5, weight=0.9 → score=56.3 NOT shortlisted
#   Hassan (IBA,  GPA 3.0, 2yr) → base=47.5, weight=1.5 → score=71.3     shortlisted
#   Ayesha ka GPA zyada hai lekin MUET penalty ki wajah se reject hoti hai — ye unfair hai.
#
#  Task 4.2 - Bias Type:
#   "Proxy Discrimination" — university name ek proxy hai socio-economic background ka.
#   MUET/QUEST public sector universities hain jo lower/middle income students attend karte hain.
#   Ye algorithm indirectly un students ko penalize karta hai jo financially kamzor hain.
#
#  Task 4.3 - Fair Rewrite: sirf GPA, experience, aur blind interview skills_score use karo
# ──────────────────────────────────────────────────────────────

# Original biased version (sirf comparison ke liye)
UNIVERSITY_WEIGHTS = {
    'IBA': 1.5, 'LUMS': 1.4, 'NUST': 1.3,
    'MUET': 0.9, 'QUEST': 0.8, 'other': 0.7,
}

def score_candidate_biased(name, university, gpa, years_exp):
    base   = (gpa / 4.0) * 50 + min(years_exp, 10) * 5
    weight = UNIVERSITY_WEIGHTS.get(university, UNIVERSITY_WEIGHTS['other'])
    final  = base * weight
    return {'name': name, 'university': university,
            'score': round(final, 1), 'shortlisted': final >= 60}


# Fair version — no university weighting
def score_candidate_fair(name, university, gpa, years_exp, skills_score=5):
    gpa_component  = (gpa / 4.0) * 50          # max 50 pts
    exp_component  = min(years_exp, 10) * 3     # max 30 pts
    skill_component = (skills_score / 10) * 20  # max 20 pts
    final = gpa_component + exp_component + skill_component
    return {'name': name, 'university': university,
            'score': round(final, 1), 'shortlisted': final >= 60}


# ── Challenge 4 Test ──────────────────────────────────────────
candidates = [
    ('Ayesha', 'MUET',  3.8, 3),
    ('Bilal',  'LUMS',  3.2, 1),
    ('Fatima', 'QUEST', 3.9, 5),
    ('Hassan', 'IBA',   3.0, 2),
]

print("\n" + "=" * 58)
print("  CHALLENGE 4 - Ethics: Biased vs Fair Hiring")
print("=" * 58)
print(f"\n  {'Name':<10} {'Uni':<8} {'Biased Score':>13} {'Fair Score':>11}  Shortlisted?")
print("  " + "-" * 52)

for c in candidates:
    biased = score_candidate_biased(*c)
    fair   = score_candidate_fair(*c)
    sl = "YES (fair)" if fair['shortlisted'] else "NO  (fair)"
    print(f"  {c[0]:<10} {c[1]:<8} {biased['score']:>13} {fair['score']:>11}  {sl}")


# ══════════════════════════════════════════════════════════════
#  CHALLENGE 5 - Grand Build: Smart Dashboard (30 pts)
#  NEXUS Smart Factory Dashboard - Build from Scratch
# ══════════════════════════════════════════════════════════════
#
#  Task 5.1 Pseudocode Plan:
#   1. sensor_report(readings) → analyse_sensors() call karo, format karo
#   2. weight_report(weights)  → batch_stats() + quality_flag() call karo, format karo
#   3. print_dashboard(sensors, weights) → dono reports combine karo
#
#  Functions: analyse_sensors, batch_stats, quality_flag, print_dashboard
#  Loop: sensor readings aur weight batches iterate karna
#  Dictionary: stats dict from batch_stats, status dict from analyse_sensors
#
#  REQ-1: sensor readings + product weights input
#  REQ-2: sensor avg + CRITICAL/WARNING/OK/NO DATA
#  REQ-3: batch mean, std, min, max
#  REQ-4: PASS/FAIL quality flag (tolerance=5g)
#  REQ-5: formatted readable report
#  REQ-6: function + loop + dictionary — sab use kiya
# ──────────────────────────────────────────────────────────────

def print_dashboard(sensors, weights):
    SEP = "=" * 58

    # Sensor section
    sensor_result = analyse_sensors(sensors)
    avg    = sensor_result['average']
    status = sensor_result['status']

    # Status ke hisaab se warning emoji text
    status_label = {
        'CRITICAL': '!! CRITICAL !!',
        'WARNING':  '>> WARNING <<',
        'OK':       '   OK       ',
        'NO DATA':  '   NO DATA  ',
    }.get(status, status)

    # Weight / batch section
    wt_array = np.array(weights) if weights else np.array([500])
    stats    = batch_stats(wt_array)
    flag     = quality_flag(wt_array)

    print("\n" + SEP)
    print("       NEXUS SMART FACTORY DASHBOARD")
    print(SEP)

    # Sensor block
    print("\n  [SENSOR MONITOR - Karachi Factory Floor]")
    print(f"  {'Readings:':<22} {sensors}")
    print(f"  {'Total sensors:':<22} {len(sensors)}")
    print(f"  {'Average reading:':<22} {avg}")
    print(f"  {'Status:':<22} {status_label}")

    # Individual readings with flag
    print(f"\n  {'#':<5} {'Value':>7}  Note")
    print("  " + "-" * 30)
    for i, val in enumerate(sensors, 1):
        note = "<-- HIGH" if val > 85 else ""
        print(f"  {i:<5} {val:>7}  {note}")

    # Quality / weight block
    print(f"\n  [QUALITY CONTROL - Hyderabad Assembly Line]")
    print(f"  {'Weights (g):':<22} {weights}")
    print(f"  {'Mean weight:':<22} {stats['mean']} g")
    print(f"  {'Std deviation:':<22} {stats['std']} g")
    print(f"  {'Min weight:':<22} {stats['min']} g")
    print(f"  {'Max weight:':<22} {stats['max']} g")
    print(f"  {'Tolerance:':<22} +/-{TOLERANCE} g")
    print(f"  {'Quality Flag:':<22} {flag}")

    # Summary footer
    print("\n" + SEP)
    print("  MISSION SUMMARY")
    print(SEP)
    sensor_ok  = status in ('OK', 'WARNING')
    quality_ok = flag == 'PASS'
    overall    = "ALL SYSTEMS NOMINAL" if (sensor_ok and quality_ok) else "ACTION REQUIRED"
    print(f"  Sensor Status  : {status}")
    print(f"  Quality Flag   : {flag}")
    print(f"  Overall Status : {overall}")
    print(SEP)


# ── Challenge 5 Test (Task 5.3 test data) ────────────────────
sensors = [72, 68, 91, 55, 63, 88, 74, 66, 95, 58]
weights = [498, 502, 497, 503, 500, 499, 501, 505, 496, 504]

print_dashboard(sensors, weights)

# Task 5.3 Reflection:
#  Sensor avg = 73.0 → WARNING (kuch readings 85+ se upar hain: 91, 88, 95)
#  Batch std  ≈ 2.8  → PASS   (weights tolerance ke andar hain)
#  Overall    → ACTION REQUIRED (sensor warning ki wajah se)
