import csv
from datetime import datetime

def export_alerts(alerts):
    # Generates a professional CSV report
    filename = f"threat_report_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "IP_Address", "Severity"])
        for alert in alerts:
            writer.writerow(alert)
    print(f"📊 Business Report generated: {filename}")

if __name__ == "__main__":
    # Sample data for your screenshot
    detected_threats = [
        [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "192.168.1.1", "CRITICAL"],
        [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "172.16.0.20", "WARNING"],
        [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "10.0.0.5", "INFO"]
    ]
    export_alerts(detected_threats)