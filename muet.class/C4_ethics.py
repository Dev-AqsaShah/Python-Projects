# ══════════════════════════════════════════════════════════════
#  CHALLENGE 4 - AI Ethics Audit (20 pts)
#  Biased Hiring Algorithm - NEXUS HR System
# ══════════════════════════════════════════════════════════════

# ── TASK 4.1: Run Original Biased Code & Observe ──────────────

UNIVERSITY_WEIGHTS = {
    'IBA':   1.5,
    'LUMS':  1.4,
    'NUST':  1.3,
    'MUET':  0.9,
    'QUEST': 0.8,
    'other': 0.7,
}

def score_candidate_biased(name, university, gpa, years_exp):
    base   = (gpa / 4.0) * 50 + min(years_exp, 10) * 5
    weight = UNIVERSITY_WEIGHTS.get(university, UNIVERSITY_WEIGHTS['other'])
    final  = base * weight
    return {'name': name, 'score': round(final, 1), 'shortlisted': final >= 60}

candidates = [
    ('Ayesha', 'MUET',  3.8, 3),
    ('Bilal',  'LUMS',  3.2, 1),
    ('Fatima', 'QUEST', 3.9, 5),
    ('Hassan', 'IBA',   3.0, 2),
]

print("=" * 58)
print("  CHALLENGE 4 - BIASED Algorithm Output (Original)")
print("=" * 58)
print(f"  {'Name':<10} {'Uni':<8} {'Score':>7}  Shortlisted?")
print("  " + "-" * 38)
for c in candidates:
    r = score_candidate_biased(*c)
    print(f"  {r['name']:<10} {c[1]:<8} {r['score']:>7}  {r['shortlisted']}")

# TASK 4.1 OBSERVATION:
#  Ayesha (MUET, GPA 3.8, 3yr) -> score = 56.2 -> NOT shortlisted (False)
#  Bilal  (LUMS, GPA 3.2, 1yr) -> score = 63.0 -> shortlisted (True)
#  Fatima (QUEST, GPA 3.9, 5yr)-> score = 59.0 -> NOT shortlisted (False)
#  Hassan (IBA,  GPA 3.0, 2yr) -> score = 71.2 -> shortlisted (True)
#
#  Ayesha ka GPA (3.8) Hassan (3.0) se kaafi zyada hai,
#  lekin sirf university ki wajah se Ayesha reject hoti hai. YE FAIR NAHI HAI.

# ── TASK 4.2: Identify the Bias ───────────────────────────────
#
#  Bias Type: PROXY DISCRIMINATION
#
#  University name ek "proxy" hai — ye directly kisi cheez ko nahi
#  dekhta, balki university ke through socio-economic background ko
#  discriminate karta hai.
#
#  MUET aur QUEST public sector universities hain jo Sindh ke
#  lower aur middle income students attend karte hain.
#  IBA aur LUMS private/elite universities hain jahan mostly
#  upper-class families ke bachche padhte hain.
#
#  Ye algorithm actually class/income discrimination kar raha hai
#  university ke naam ki aad mein — ye legally aur ethically galat hai.
#
#  Sabse zyada nuksaan: MUET/QUEST ke students jo academically
#  outstanding hain (jaise Ayesha GPA 3.8) lekin reject ho jate hain.

# ── TASK 4.3: AI Prompt for Fair Rewrite ──────────────────────
#
#  PROMPT:
#  "Rewrite this score_candidate() function to remove university bias.
#   The new version should only use:
#   - GPA (out of 4.0)
#   - years_exp (years of experience)
#   - skills_score (0-10, from blind interview, default=5)
#   No university weighting at all.
#   Scoring: GPA contributes 50 pts max, experience 30 pts max,
#   skills 20 pts max. Shortlisted if total >= 60."

# ── Fair Code (AI Output) ──────────────────────────────────────

def score_candidate_fair(name, university, gpa, years_exp, skills_score=5):
    gpa_pts   = (gpa / 4.0) * 50           # max 50 pts
    exp_pts   = min(years_exp, 10) * 3     # max 30 pts
    skill_pts = (skills_score / 10) * 20   # max 20 pts
    final     = gpa_pts + exp_pts + skill_pts
    return {
        'name':        name,
        'university':  university,
        'score':       round(final, 1),
        'shortlisted': final >= 60
    }

print("\n  FAIR Algorithm Output (Rewritten)")
print("  " + "-" * 50)
print(f"  {'Name':<10} {'Uni':<8} {'Biased':>7} {'Fair':>7}  Shortlisted (Fair)?")
print("  " + "-" * 50)
for c in candidates:
    biased = score_candidate_biased(*c)
    fair   = score_candidate_fair(*c)
    print(f"  {c[0]:<10} {c[1]:<8} {biased['score']:>7} {fair['score']:>7}  {fair['shortlisted']}")

print("=" * 58)

# FAIR RESULTS:
#  Ayesha (MUET,  GPA 3.8, 3yr) -> Fair score = 66.5 -> YES shortlisted
#  Bilal  (LUMS,  GPA 3.2, 1yr) -> Fair score = 53.0 -> NO
#  Fatima (QUEST, GPA 3.9, 5yr) -> Fair score = 73.8 -> YES shortlisted
#  Hassan (IBA,   GPA 3.0, 2yr) -> Fair score = 53.5 -> NO
#
#  Ab merit ke hisaab se decision ho raha hai, university name se nahi.
