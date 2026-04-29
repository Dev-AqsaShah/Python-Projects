# ══════════════════════════════════════════════════════════════
#  CHALLENGE 2 - NumPy Production Stats (25 pts)
#  Quality Control Dashboard - Hyderabad Assembly Line
# ══════════════════════════════════════════════════════════════

import numpy as np

batch_A = np.array([498, 502, 497, 503, 500, 499, 501, 505, 496, 504])
batch_B = np.array([510, 523, 488, 531, 476, 519, 482, 527, 491, 515])
batch_C = np.array([500, 500, 500, 500, 500, 500, 500, 500, 500, 500])

TOLERANCE = 5

# ── TASK 2.1: Plan (Plain English) ────────────────────────────
#
#  batch_stats(batch):
#    - Is function ko ek numpy array milti hai (product weights)
#    - Hamen mean (average), std (standard deviation), min, max chahiye
#    - Numpy functions: np.mean(), np.std(), np.min(), np.max()
#    - Return: ek dictionary with these 4 values
#
#  quality_flag(batch, tolerance):
#    - Agar batch ki std (variation) <= tolerance (5g) ho to 'PASS'
#    - Agar std > tolerance ho to 'FAIL' (weights zyada vary kar rahe hain)
#    - Numpy function: np.std()

# ── TASK 2.2: AI Prompt Used ───────────────────────────────────
#
#  PROMPT:
#  "Complete these two Python functions using numpy.
#   Do not change the function signatures.
#
#   def batch_stats(batch):
#       # Return a dict with keys: mean, std, min, max
#       # All values rounded to 2 decimal places
#       pass
#
#   def quality_flag(batch, tolerance=5):
#       # Return 'PASS' if np.std(batch) <= tolerance, else 'FAIL'
#       pass"

# ── AI's Completed Functions ───────────────────────────────────

def batch_stats(batch):
    return {
        'mean': round(float(np.mean(batch)), 2),
        'std':  round(float(np.std(batch)),  2),
        'min':  int(np.min(batch)),
        'max':  int(np.max(batch)),
    }

def quality_flag(batch, tolerance=TOLERANCE):
    return 'PASS' if np.std(batch) <= tolerance else 'FAIL'


# ── TASK 2.3: Run and Interpret Results ───────────────────────

print("=" * 58)
print("  CHALLENGE 2 - Quality Control Dashboard Output")
print("=" * 58)
print(f"  {'Batch':<8} {'Mean':>7} {'Std':>7} {'Min':>6} {'Max':>6}  Flag")
print("  " + "-" * 46)

for name, b in [('A', batch_A), ('B', batch_B), ('C', batch_C)]:
    s    = batch_stats(b)
    flag = quality_flag(b)
    print(f"  Batch {name}  {s['mean']:>7} {s['std']:>7} {s['min']:>6} {s['max']:>6}  {flag}")

print("=" * 58)

# TASK 2.3 ANSWERS:
#
#  Batch A -> std = 2.87 -> PASS
#    Variation kam hai (2.87 < 5), weights 500g ke aas paas hain — acceptable
#
#  Batch B -> std = 19.09 -> FAIL
#    Variation bahut zyada hai (19.09 > 5), weights 476g se 531g tak hain — reject
#
#  Batch C -> std = 0.0 -> PASS
#    Saari 10 values exactly 500g hain, isliye std = 0
#    Real factory mein ye UNREALISTIC hai — machines mein hamesha thodi variation hoti hai.
#    std=0 ka matlab hai ya sensor broken hai ya data fake hai.
