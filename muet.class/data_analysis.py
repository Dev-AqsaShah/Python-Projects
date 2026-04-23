# ─────────────────────────────────────────────
#  Monthly Sales Data Analysis (no imports)
# ─────────────────────────────────────────────

# Raw monthly sales data: month -> units sold
sales_data = {
    "January":   320,
    "February":  275,
    "March":     410,
    "April":     390,
    "May":       520,
    "June":      480,
    "July":      610,
    "August":    575,
    "September": 430,
    "October":   365,
    "November":  490,
    "December":  700,
}


# ── Helper functions ──────────────────────────

def mean(values):
    return sum(values) / len(values)

def median(values):
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]

def std_dev(values):
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return variance ** 0.5

def classify(units, avg):
    if units >= avg * 1.2:
        return "High"
    elif units >= avg * 0.8:
        return "Average"
    else:
        return "Low"


# ── Core analysis function ────────────────────

def analyse_data(data):
    values = list(data.values())
    avg = mean(values)
    return {
        "total":    sum(values),
        "mean":     avg,
        "median":   median(values),
        "std_dev":  std_dev(values),
        "max":      max(values),
        "max_month": max(data, key=data.get),
        "min":      min(values),
        "min_month": min(data, key=data.get),
    }


# ── Monthly summary table ─────────────────────

stats = analyse_data(sales_data)
avg   = stats["mean"]

print("=" * 52)
print("       MONTHLY SALES ANALYSIS REPORT")
print("=" * 52)
print(f"{'Month':<12} {'Units Sold':>12} {'vs Average':>12} {'Status':>10}")
print("-" * 52)

for month, units in sales_data.items():
    diff   = units - avg
    sign   = "+" if diff >= 0 else ""
    status = classify(units, avg)
    print(f"{month:<12} {units:>12,} {sign + str(round(diff)):>12} {status:>10}")

# ── Statistical summary ───────────────────────

print("=" * 52)
print("  STATISTICAL SUMMARY")
print("=" * 52)
print(f"  {'Total annual sales:':<24} {stats['total']:>8,} units")
print(f"  {'Monthly mean:':<24} {stats['mean']:>8.1f} units")
print(f"  {'Median:':<24} {stats['median']:>8.1f} units")
print(f"  {'Std deviation:':<24} {stats['std_dev']:>8.2f}")
print(f"  {'Best month:':<24} {stats['max_month']:>8}  ({stats['max']:,} units)")
print(f"  {'Worst month:':<24} {stats['min_month']:>8}  ({stats['min']:,} units)")

# ── Quarter breakdown ─────────────────────────

quarters = {
    "Q1 (Jan-Mar)": ["January",   "February", "March"],
    "Q2 (Apr-Jun)": ["April",     "May",      "June"],
    "Q3 (Jul-Sep)": ["July",      "August",   "September"],
    "Q4 (Oct-Dec)": ["October",   "November", "December"],
}

print("=" * 52)
print("  QUARTERLY BREAKDOWN")
print("=" * 52)
print(f"  {'Quarter':<16} {'Total':>8} {'Average':>10} {'Trend':>10}")
print("  " + "-" * 46)

prev_total = None
for qname, months in quarters.items():
    q_total = sum(sales_data[m] for m in months)
    q_avg   = q_total / len(months)
    if prev_total is None:
        trend = "--"
    else:
        pct   = (q_total - prev_total) / prev_total * 100
        trend = f"{'UP' if pct >= 0 else 'DN'} {abs(pct):.1f}%"
    prev_total = q_total
    print(f"  {qname:<16} {q_total:>8,} {q_avg:>10.1f} {trend:>10}")

print("=" * 52)
print("  ANALYSIS COMPLETE")
print("=" * 52)
