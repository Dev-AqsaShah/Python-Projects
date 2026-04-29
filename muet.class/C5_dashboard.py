# ══════════════════════════════════════════════════════════════
#  CHALLENGE 5 - Grand Build: Smart Dashboard (30 pts)
#  NEXUS Smart Factory Dashboard - Build from Scratch
# ══════════════════════════════════════════════════════════════

import numpy as np

# ── TASK 5.1: Plan (Pseudocode / Function Diagram) ────────────
#
#  FUNCTIONS NEEDED:
#    1. analyse_sensors(readings)
#         -> Input:  list of sensor readings
#         -> Output: dict {average, status}
#         -> Uses:   loop (sum), if/elif/else
#
#    2. batch_stats(weights)
#         -> Input:  numpy array of weights
#         -> Output: dict {mean, std, min, max}
#         -> Uses:   np.mean, np.std, np.min, np.max
#
#    3. quality_flag(weights, tolerance)
#         -> Input:  numpy array, tolerance value
#         -> Output: 'PASS' or 'FAIL'
#         -> Uses:   np.std
#
#    4. print_dashboard(sensors, weights)
#         -> Calls all 3 above
#         -> Prints formatted report
#         -> Uses:   loop (sensor readings), dict (stats), function calls
#
#  OUTPUT FORMAT:
#    ============================================================
#    NEXUS SMART FACTORY DASHBOARD
#    ============================================================
#    [SENSOR MONITOR]
#      Average, Status, Individual readings with HIGH flag
#    [QUALITY CONTROL]
#      Mean, Std, Min, Max, Quality Flag
#    [SUMMARY]
#      Overall status

# ── TASK 5.2: Prompt Chain ─────────────────────────────────────
#
#  PROMPT 1 (Sensor function):
#  "Write a Python function analyse_sensors(readings) that:
#   - Returns {'average': 0, 'status': 'NO DATA'} if list is empty
#   - Calculates average of the list
#   - Returns status: CRITICAL if avg>85, WARNING if avg>60, else OK
#   - Returns dict with average (rounded 2 decimal) and status"
#
#  PROMPT 2 (Batch stats + quality flag with numpy):
#  "Write two numpy functions:
#   1. batch_stats(batch) -> dict with mean, std, min, max (all rounded to 2dp)
#   2. quality_flag(batch, tolerance=5) -> 'PASS' if std<=tolerance else 'FAIL'
#   Use numpy functions only."
#
#  PROMPT 3 (Dashboard formatter):
#  "Write a print_dashboard(sensors, weights) function that:
#   - Calls analyse_sensors and shows average + status
#   - Lists each sensor reading and marks ones >85 as HIGH
#   - Calls batch_stats and quality_flag on weights array
#   - Prints a clean formatted report with sections and separators
#   - Ends with a MISSION SUMMARY section"

# ══════════════════════════════════════════════════════════════
#  FINAL WORKING CODE (Combined from all 3 prompts)
# ══════════════════════════════════════════════════════════════

TOLERANCE = 5   # grams

# -- Function 1: Sensor Monitor (from C1 fix) ------------------
def analyse_sensors(readings):
    if not readings:
        return {'average': 0, 'status': 'NO DATA'}
    average = sum(readings) / len(readings)
    if average > 85:
        status = 'CRITICAL'
    elif average > 60:
        status = 'WARNING'
    else:
        status = 'OK'
    return {'average': round(average, 2), 'status': status}

# -- Function 2: Batch Stats (from C2) -------------------------
def batch_stats(weights):
    arr = np.array(weights)
    return {
        'mean': round(float(np.mean(arr)), 2),
        'std':  round(float(np.std(arr)),  2),
        'min':  int(np.min(arr)),
        'max':  int(np.max(arr)),
    }

# -- Function 3: Quality Flag (from C2) ------------------------
def quality_flag(weights, tolerance=TOLERANCE):
    return 'PASS' if np.std(weights) <= tolerance else 'FAIL'

# -- Function 4: Dashboard Printer (C5 new) --------------------
def print_dashboard(sensors, weights):
    LINE = "=" * 58
    DASH = "-" * 40

    sensor_data = analyse_sensors(sensors)
    avg    = sensor_data['average']
    status = sensor_data['status']

    wt_array = np.array(weights)
    stats    = batch_stats(wt_array)
    flag     = quality_flag(wt_array)

    # Status display label
    status_display = {
        'CRITICAL': '!! CRITICAL !!  (EMERGENCY - STOP LINE)',
        'WARNING':  '>> WARNING <<   (Alert supervisor)',
        'OK':       '   OK           (All normal)',
        'NO DATA':  '   NO DATA      (No readings received)',
    }.get(status, status)

    print("\n" + LINE)
    print("       NEXUS SMART FACTORY DASHBOARD")
    print("       NEXUS Engineering Solutions")
    print(LINE)

    # ── Sensor Section ──────────────────────────────────────
    print("\n  [SENSOR MONITOR - Karachi Factory Floor]")
    print("  " + DASH)
    print(f"  Total Sensors  : {len(sensors)}")
    print(f"  Average        : {avg}")
    print(f"  Status         : {status_display}")
    print(f"\n  {'No.':<5} {'Reading':>8}  Alert")
    print("  " + "-" * 25)
    for i, val in enumerate(sensors, 1):           # loop use kiya (REQ-6)
        alert = "<-- HIGH ALERT" if val > 85 else ""
        print(f"  {i:<5} {val:>8}  {alert}")

    # ── Quality Control Section ──────────────────────────────
    print(f"\n  [QUALITY CONTROL - Hyderabad Assembly Line]")
    print("  " + DASH)
    print(f"  Mean Weight    : {stats['mean']} g")    # dict use kiya (REQ-6)
    print(f"  Std Deviation  : {stats['std']} g")
    print(f"  Min Weight     : {stats['min']} g")
    print(f"  Max Weight     : {stats['max']} g")
    print(f"  Tolerance      : +/-{TOLERANCE} g")
    print(f"  Quality Flag   : {flag}")

    # ── Summary Section ──────────────────────────────────────
    sensor_ok  = status in ('OK', 'WARNING')
    quality_ok = flag == 'PASS'

    if status == 'CRITICAL' or not quality_ok:
        overall = "IMMEDIATE ACTION REQUIRED"
    elif status == 'WARNING':
        overall = "MONITOR CLOSELY - WARNING ACTIVE"
    else:
        overall = "ALL SYSTEMS NOMINAL"

    print("\n" + LINE)
    print("  MISSION SUMMARY")
    print(LINE)
    print(f"  Sensor Status  : {status}")
    print(f"  Quality Flag   : {flag}")
    print(f"  Overall Status : {overall}")
    print(LINE + "\n")


# ── TASK 5.3: Test with given data ────────────────────────────
sensors = [72, 68, 91, 55, 63, 88, 74, 66, 95, 58]
weights = [498, 502, 497, 503, 500, 499, 501, 505, 496, 504]

print_dashboard(sensors, weights)

# TASK 5.3 REFLECTION:
#
#  Dashboard output shows:
#    Sensor avg = 73.0  -> WARNING (readings 91, 88, 95 are HIGH)
#    Batch std  = 2.87  -> PASS   (weights within +/-5g tolerance)
#    Overall    -> MONITOR CLOSELY - WARNING ACTIVE
#
#  What surprised us most:
#    Vibecoding mein sab se surprising ye tha ke agar prompt clear ho
#    to AI bilkul sahi structure deta hai — lekin hamen har output
#    verify karna parta hai kyunki AI kabhi kabhi logic galat kar deta hai.
#
#  What we would change with more time:
#    - File se data load karna (CSV sensor logs)
#    - Timestamp add karna (kis waqt reading aayi)
#    - Email alert system add karna jab status CRITICAL ho
