# 🛡️ Sentinel: Real-Time Log Analytics
A high-performance anomaly detection system designed to identify suspicious network traffic patterns using sliding window algorithms.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Logic:** Sliding Window Heuristics, Deque-based Memory Management
- **Domain:** Cybersecurity & Data Engineering

## 📊 How it Works
Sentinel monitors incoming IP requests and maintains a temporal window for each source. If the request frequency exceeds a defined threshold within a specific timeframe, an alert is triggered.



## 🚀 Key Features
- **$O(1)$ Complexity:** Fast window sliding using `collections.deque`.
- **Memory Efficient:** Automatically purges stale logs to prevent memory leaks.
- **Scalable:** Uses hash-mapping to track thousands of unique IP addresses.
