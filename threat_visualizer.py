import matplotlib.pyplot as plt
import pandas as pd
import os

# 1. Verification & Loading
file_path = 'threat_report_20260307.csv'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found! Run threat_analysis.py first.")
else:
    try:
        df = pd.read_csv(file_path)
        
        # 2. Smart Column Detection (Fixes the 'status' error)
        # This looks for 'status', 'level', or the 2nd column automatically
        target_col = 'status' if 'status' in df.columns else df.columns[1]
        threat_counts = df[target_col].value_counts()

        # 3. Generate Professional Bar Chart
        plt.figure(figsize=(10, 6))
        colors = ['#d62728', '#ff7f0e', '#1f77b4'] # Red, Orange, Blue
        threat_counts.plot(kind='bar', color=colors[:len(threat_counts)])

        plt.title('Security Threat Distribution - Sharath T E', fontsize=14, fontweight='bold')
        plt.xlabel('Severity Level', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        # 4. Save to Project Sentinel Folder
        plt.tight_layout()
        plt.savefig('threat_chart_day17.png')
        print(f"Success! Chart generated using column: '{target_col}'")
        plt.show()

    except Exception as e:
        print(f"Technical Error: {e}")