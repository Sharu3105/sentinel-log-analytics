import pandas as pd

def check_for_critical_threats(csv_file):
    print(f"--- Sentinel Alert System Scanning: {csv_file} ---")
    try:
        df = pd.read_csv(csv_file)
        # Filter for Critical status
        critical_threats = df[df.iloc[:, 1].str.contains('Critical', case=False, na=False)]
        
        if not critical_threats.empty:
            print(f"🚨 ALERT: {len(critical_threats)} Critical Threats Detected!")
            for index, row in critical_threats.iterrows():
                print(f"  -> Action Required: Threat at {row[0]}")
            return True
        else:
            print("✅ System Secure: No Critical threats found.")
            return False
    except Exception as e:
        print(f"Error in Alert Engine: {e}")
        return False

if __name__ == "__main__":
    check_for_critical_threats('threat_report_20260307.csv')