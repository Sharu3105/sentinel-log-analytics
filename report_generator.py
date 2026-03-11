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
    
    import pandas as pd
import os
from datetime import datetime

def generate_sentinel_report(csv_file):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Analysis must run first.")
        return

    # Load and prepare data
    df = pd.read_csv(csv_file)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create HTML table with Bootstrap styling
    html_table = df.to_html(classes='table table-dark table-hover', index=False)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sentinel Intelligence Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }}
            .container {{ margin-top: 50px; }}
            .header-box {{ border-left: 5px solid #0d6efd; padding-left: 20px; margin-bottom: 40px; }}
            .stats-card {{ background-color: #1e1e1e; border: none; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header-box">
                <h1 class="display-4">Project Sentinel: Security Report</h1>
                <p class="lead">Lead Architect: <strong>Sharath T E</strong></p>
                <p class="text-muted">Generated on: {timestamp}</p>
            </div>
            
            <div class="card stats-card shadow-lg">
                <div class="card-body">
                    <h4 class="card-title text-info mb-4">Detected Threats Log</h4>
                    {html_table}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    with open("sentinel_web_report.html", "w") as f:
        f.write(html_template)
    
    print("🚀 Web Report generated successfully: sentinel_web_report.html")

if __name__ == "__main__":
    generate_sentinel_report('threat_report_20260307.csv')
    