import pandas as pd

# ══════════════════════════════════════════════════════════════
#  TITANIC DATASET - Pandas Analysis
#  Dataset: 891 rows, 12 columns
# ══════════════════════════════════════════════════════════════

df = pd.read_csv('Titanic-Dataset.csv')

# ──────────────────────────────────────────────────────────────
#  STEP 1: BASIC EXPLORATION
# ──────────────────────────────────────────────────────────────
print("=" * 60)
print("  STEP 1: BASIC EXPLORATION")
print("=" * 60)

print(f"\nDataset Shape  : {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Column Names   : {list(df.columns)}")

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Last 3 Rows ---")
print(df.tail(3))

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

# ──────────────────────────────────────────────────────────────
#  STEP 2: MISSING VALUES
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 2: MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)

missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Missing %': missing_pct
})
missing_df = missing_df[missing_df['Missing Count'] > 0]
print(missing_df)

# Age ki missing values -> median se fill karo
df['Age'] = df['Age'].fillna(df['Age'].median())

# Embarked ki 2 missing values -> most common value (mode) se fill karo
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin mein 687 missing hain (77%) -> column drop karo
df.drop(columns=['Cabin'], inplace=True)

print("\nAfter Cleaning — Missing Values:")
print(df.isnull().sum())

# ──────────────────────────────────────────────────────────────
#  STEP 3: DATA SELECTION & FILTERING
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 3: DATA SELECTION & FILTERING")
print("=" * 60)

# Single column select karna
print("\n--- Passenger Names (first 5) ---")
print(df['Name'].head())

# Multiple columns select karna
print("\n--- Name, Age, Sex (first 5) ---")
print(df[['Name', 'Age', 'Sex']].head())

# Condition se filter karna — sirf females
females = df[df['Sex'] == 'female']
print(f"\nTotal Females  : {len(females)}")

# Condition se filter — age > 50 aur survived
old_survivors = df[(df['Age'] > 50) & (df['Survived'] == 1)]
print(f"Survivors > 50 : {len(old_survivors)}")

# 1st class passengers
first_class = df[df['Pclass'] == 1]
print(f"1st Class Total: {len(first_class)}")

# loc — row aur column naam se select karna
print("\n--- loc: rows 0-4, specific columns ---")
print(df.loc[0:4, ['Name', 'Sex', 'Age', 'Survived']])

# iloc — row aur column index number se select karna
print("\n--- iloc: first 3 rows, first 4 columns ---")
print(df.iloc[0:3, 0:4])

# ──────────────────────────────────────────────────────────────
#  STEP 4: USEFUL STATISTICS & INSIGHTS
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 4: USEFUL STATISTICS & INSIGHTS")
print("=" * 60)

total       = len(df)
survived    = df['Survived'].sum()
not_survived = total - survived

print(f"\nTotal Passengers : {total}")
print(f"Survived         : {survived}  ({survived/total*100:.1f}%)")
print(f"Did Not Survive  : {not_survived}  ({not_survived/total*100:.1f}%)")

print(f"\nAverage Age      : {df['Age'].mean():.1f} years")
print(f"Youngest         : {df['Age'].min():.0f} years")
print(f"Oldest           : {df['Age'].max():.0f} years")

print(f"\nAverage Fare     : ${df['Fare'].mean():.2f}")
print(f"Most Expensive   : ${df['Fare'].max():.2f}")
print(f"Cheapest Ticket  : ${df['Fare'].min():.2f}")

# Value counts — kitne male, kitne female
print("\n--- Passenger Count by Sex ---")
print(df['Sex'].value_counts())

# Value counts — class distribution
print("\n--- Passenger Count by Class ---")
print(df['Pclass'].value_counts().sort_index())

# ──────────────────────────────────────────────────────────────
#  STEP 5: GROUPBY — GROUP KE HISAAB SE ANALYSIS
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 5: GROUPBY ANALYSIS")
print("=" * 60)

# Survival rate by Sex
print("\n--- Survival Rate by Sex ---")
sex_survival = df.groupby('Sex')['Survived'].mean() * 100
print(sex_survival.round(1).to_string())

# Survival rate by Passenger Class
print("\n--- Survival Rate by Passenger Class ---")
class_survival = df.groupby('Pclass')['Survived'].mean() * 100
print(class_survival.round(1).to_string())

# Average age by class
print("\n--- Average Age by Passenger Class ---")
age_by_class = df.groupby('Pclass')['Age'].mean()
print(age_by_class.round(1).to_string())

# Multiple stats ek saath — groupby + agg
print("\n--- Detailed Stats by Sex ---")
detailed = df.groupby('Sex').agg(
    Total_Passengers = ('PassengerId', 'count'),
    Survived_Count   = ('Survived',    'sum'),
    Survival_Rate_pct= ('Survived',    lambda x: round(x.mean()*100, 1)),
    Avg_Age          = ('Age',         lambda x: round(x.mean(), 1)),
    Avg_Fare         = ('Fare',        lambda x: round(x.mean(), 2)),
)
print(detailed)

# Embarked port se kitne log aaye
print("\n--- Passengers by Embarkation Port ---")
port_names = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
embarked_counts = df['Embarked'].value_counts()
for port, count in embarked_counts.items():
    print(f"  {port_names.get(port, port):<14}: {count} passengers")

# ──────────────────────────────────────────────────────────────
#  STEP 6: NEW COLUMNS BANANA (FEATURE ENGINEERING)
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 6: NEW COLUMNS ADD KARNA")
print("=" * 60)

# Age groups banana
def age_group(age):
    if age < 13:
        return 'Child'
    elif age < 18:
        return 'Teen'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)
print("\n--- Survival Rate by Age Group ---")
print(df.groupby('AgeGroup')['Survived'].mean().mul(100).round(1).to_string())

# Family size column
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # +1 for self
print("\n--- Survival Rate by Family Size ---")
fam_survival = df.groupby('FamilySize')['Survived'].mean().mul(100).round(1)
print(fam_survival.to_string())

# Travel Alone column
df['TravelAlone'] = df['FamilySize'].apply(lambda x: 'Yes' if x == 1 else 'No')
print("\n--- Solo vs Group Travelers ---")
print(df['TravelAlone'].value_counts())

# ──────────────────────────────────────────────────────────────
#  STEP 7: SORTING & TOP RECORDS
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 7: SORTING & TOP RECORDS")
print("=" * 60)

# Sabse zyada fare dene wale 5 passengers
print("\n--- Top 5 Most Expensive Tickets ---")
top_fare = df[['Name', 'Pclass', 'Fare', 'Survived']].sort_values('Fare', ascending=False).head(5)
print(top_fare.to_string(index=False))

# Sabse young survivors
print("\n--- 5 Youngest Survivors ---")
young_survivors = df[df['Survived'] == 1][['Name', 'Sex', 'Age', 'Pclass']].sort_values('Age').head(5)
print(young_survivors.to_string(index=False))

# ──────────────────────────────────────────────────────────────
#  STEP 8: FINAL SUMMARY
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 8: FINAL DATASET OVERVIEW")
print("=" * 60)
print(f"\nFinal Shape      : {df.shape}")
print(f"Columns          : {list(df.columns)}")
print("\n--- Sample of Final Dataset (first 5 rows) ---")
print(df[['Name', 'Sex', 'Age', 'Pclass', 'Survived', 'AgeGroup', 'FamilySize', 'TravelAlone']].head().to_string(index=False))
print("\n" + "=" * 60)
print("  ANALYSIS COMPLETE")
print("=" * 60)

# ──────────────────────────────────────────────────────────────
#  STEP 9: DATA STORE KARNA — AUR KYU KARTE HAIN
# ──────────────────────────────────────────────────────────────
#
#  PROBLEM:
#    Ye poora kaam (cleaning, missing values fill, naye columns)
#    sirf computer ki RAM mein tha.
#    Program band karo — sab KHATAM. Kal dobara se karna parega.
#
#  SOLUTION: Store karo — file mein save karo
#
#  3 REAL REASONS:
#    1. SAVE TIME   -> Cleaning dobara nahi karni — cleaned file se seedha shuru
#    2. SHARE KARO  -> Sir ya teammate ko cleaned data do, raw nahi
#    3. NEXT STEP   -> Machine Learning ke liye cleaned data chahiye hoti hai
#
# ──────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  STEP 9: DATA STORE KARNA")
print("=" * 60)

# ── METHOD 1: CSV file mein save karna (sabse common) ─────────
# index=False matlab row numbers (0,1,2...) save mat karo
df.to_csv('Titanic-Cleaned.csv', index=False)
print("\n[1] CSV saved   -> Titanic-Cleaned.csv")
print("    Kyun CSV?    -> Excel, Python, R — sab CSV open kar sakte hain")

# ── METHOD 2: Excel file mein save karna ──────────────────────
df.to_excel('Titanic-Cleaned.xlsx', index=False, sheet_name='Titanic Data')
print("\n[2] Excel saved -> Titanic-Cleaned.xlsx")
print("    Kyun Excel?  -> Sir ya manager ko bhejna ho, Excel se easily dekhte hain")

# ── METHOD 3: Specific columns hi save karna ──────────────────
important_cols = ['Name', 'Sex', 'Age', 'Pclass', 'Survived',
                  'Fare', 'AgeGroup', 'FamilySize', 'TravelAlone']
df[important_cols].to_csv('Titanic-Important-Cols.csv', index=False)
print("\n[3] CSV saved   -> Titanic-Important-Cols.csv")
print("    Kyun?        -> Sirf zaroori columns — Ticket, PassengerId jaise useless cols hata diye")

# ── METHOD 4: Sirf survived passengers save karna ─────────────
df[df['Survived'] == 1].to_csv('Titanic-Survivors-Only.csv', index=False)
print("\n[4] CSV saved   -> Titanic-Survivors-Only.csv")
print("    Kyun?        -> Sirf survivors ka data — specific analysis ke liye")

# ── VERIFY: Saved file wapas load karke check karo ────────────
print("\n--- Verification: Saved file wapas load karo ---")
df_loaded = pd.read_csv('Titanic-Cleaned.csv')
print(f"Loaded Shape    : {df_loaded.shape}")
print(f"Columns         : {list(df_loaded.columns)}")
print(f"Missing Values  : {df_loaded.isnull().sum().sum()} (should be 0)")

print("\n" + "=" * 60)
print("  SUMMARY: Konsi File Kab Use Karein")
print("=" * 60)
summary = {
    'Titanic-Cleaned.csv'          : 'Full cleaned dataset — next project mein use karo',
    'Titanic-Cleaned.xlsx'         : 'Sir ko submit karo — Excel mein clearly dikhta hai',
    'Titanic-Important-Cols.csv'   : 'ML model ke liye — sirf useful features',
    'Titanic-Survivors-Only.csv'   : 'Survivors ka alag analysis karna ho to',
}
for fname, reason in summary.items():
    print(f"  {fname:<35} -> {reason}")
print("=" * 60)
