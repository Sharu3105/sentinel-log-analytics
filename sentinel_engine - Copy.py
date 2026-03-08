import collections
import time
import random

class Sentinel:
    """
    Sentinel: A Real-Time Anomaly Detection Engine.
    Uses sliding window logic to detect high-frequency traffic patterns.
    """
    def __init__(self, threshold=5, window_seconds=10):
        self.threshold = threshold
        self.window_seconds = window_seconds
        self.log_history = collections.defaultdict(collections.deque) 

    def analyze_traffic(self, ip_address):
        now = time.time()
        window = self.log_history[ip_address]
        
        # Add current hit
        window.append(now)

        # Remove logs older than the window period
        while window and window[0] < now - self.window_seconds:
            window.popleft()

        # Check for anomalies
        if len(window) > self.threshold:
            return f"⚠️ ALERT: Potential DDoS/Brute Force from {ip_address}! ({len(window)} hits)"
        return f"✅ Status: Normal for {ip_address}"

# --- Simulation Block ---
if __name__ == "__main__":
    monitor = Sentinel(threshold=4, window_seconds=2)
    test_ip = "192.168.1.105"
    
    print(f"Starting analysis for {test_ip}...")
    for i in range(7):
        print(monitor.analyze_traffic(test_ip))
        time.sleep(0.3) # Simulating rapid requests
