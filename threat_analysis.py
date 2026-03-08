import pandas as pd

# 1. Load the data you generated on Day 15
try:
    df = pd.read_csv('threat_report_20260307.csv')
    print("✅ Successfully loaded Day 15 Threat Report\n")
except FileNotFoundError:
    print("❌ Error: CSV file not found. Run report_generator.py first.")
    exit()

# 2. Basic Inspection
print("--- Data Overview ---")
print(df.head()) # Shows the first 5 rows

# 3. Frequency Analysis (Find the top attacker)
print("\n--- Threat Frequency by IP ---")
ip_counts = df['IP_Address'].value_counts()
print(ip_counts)

# 4. Severity Distribution (Business Metric)
print("\n--- Severity Summary ---")
severity_summary = df['Severity'].value_counts()
print(severity_summary)

# 5. Export a Summary Text File
with open('daily_summary.txt', 'w') as f:
    f.write(f"Total Threats Detected: {len(df)}\n")
    f.write(f"Top Attacker: {ip_counts.index[0]} with {ip_counts.values[0]} attempts\n")
print("\n📝 daily_summary.txt has been created for your records.")