import random
import time
from sentinel_engine import Sentinel

def run_test():
    # threshold=5 hits in 10 seconds triggers alert
    monitor = Sentinel(threshold=5, window_seconds=10)
    
    # Safe IPs and one malicious "Attacker" IP
    traffic_sources = ["192.168.1.1", "10.0.0.5", "172.16.0.20"]
    attacker = "45.77.12.101"
    
    print("🚀 Sentinel Simulation Started...")
    
    for i in range(40):
        # 80% chance normal traffic, 20% chance attacker spike
        ip = attacker if random.random() < 0.2 else random.choice(traffic_sources)
        
        status = monitor.analyze_traffic(ip)
        
        if "ALERT" in status:
            print(f"[{i}] 🚨 {status}")
        else:
            if i % 5 == 0: print(f"[{i}] Mapping traffic: {ip} - OK")
            
        time.sleep(0.2) # Faster simulation

if __name__ == "__main__":
    run_test()
