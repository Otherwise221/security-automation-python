# security-automation-python
## Independent Study Project -- Jan - May 2026 -- UNK

# File Analysis & Malicious Indicator Detection Tool

A Python-based security automation tool built for static file analysis and log-based threat detection. This tool simulates core triage workflows used in SOC environments by scanning files for malicious indicators, generating and comparing file hashes, managing a dynamic threat keyword library, and detecting suspicious patterns in system log files.

---

## Background

This project was developed as part of an independent study in Python Security Automation. The goal was to build a practical, menu-driven tool that automates common malware triage and log analysis tasks — reducing manual analysis time and improving consistency in threat detection.

---

## Features

| Option | Function |
|--------|----------|
| A | Scan a file for malicious indicator keywords |
| B | Generate a SHA-256 hash of a file and store it in the hash library |
| E | Add a new keyword to the malicious indicator list |
| F | Delete a specific keyword or slear the entire keyword list | 
| G | Compare a file's hash against the stored hash library |
| Z | Quit |

SuspiciousPatterns.py — Log Analysis Tool
A separate module that ingests .csv, .txt, or .xlsx log files and performs three detections:

Malicious IP Detection — flags IPs matching a known bad IP list (bad_IPs.txt)
Unusual Login Detection — identifies LOGIN events occurring between 6PM–6AM
Frequent Login Detection — flags users with 3+ logins within a 2-minute window (brute force indicator)

---

## How It Works

### Malicious Indicator Scanning
The tool reads a target file line by line and checks each line against a customizable keyword list (Keywords.txt). Keywords represent known malicious indicators such as tool names, suspicious executables, and attacker techniques. Matches are reported with the line number, keyword found, and the full line content.

**Sample keywords include:**
`mimikatz`, `rundll32`, `mshta`, `wscript`, `powershell.exe`, `keylogger`, `rootkit`, `payload`, `tor`, `exfil`

### Hash Generation & Comparison
Files are hashed using SHA-256 via Python's hashlib module. Generated hashes are stored in hashLibrary.txt. The comparison feature checks whether a given file's hash matches any stored hash — useful for identifying known malicious files or verifying file integrity.

### Dynamic Keyword Management
Users can add new malicious indicators or remove existing ones at runtime. Duplicate detection prevents redundant entries. Deletion supports both targeted removal (single keyword) and full library wipe. This simulates how threat intelligence feeds update and retire detection rules in real SOC environments.

### Log-Based Suspicious Pattern Detection
The log analysis module reads structured log files using pandas and performs behavioral analysis across three threat categories. Expected log columns: Timestamp, Username, IP Address, Event Type, Status, Location, Notes.

---

## File Structure

```
├── Analysis.py              # Main tool — menu-driven interface
├── Suspicious_Patterns.py   # Log analysis tool - IP, logintime, brute force detection
├── Malicious_Indicators.py  # Early prototype of the indicator scanner
├── keyword_maker.py         # Standalone keyword management utility
├── Keywords.txt             # Malicious indicator keyword library
├── bad_IPs.txt              # Known malicious IP address list
├── hashLibrary.txt          # Stored SHA-256 file hashes
└── file.txt                 # Sample test file
```

---

## Getting Started

**Requirements:** Python 3.x (no external libraries needed)

```bash
# Clone the repository
git clone https://github.com/Otherwise221/security-automation-python.git
cd security-automation-python

# Run the tool
python Analysis.py

# Run the log analysis tool
python Suspicious_Patterns.py
```

---

## Security Concepts Demonstrated

- **Static file analysis** — scanning file contents against known threat indicators
- **File integrity checking** — SHA-256 hashing to detect file tampering or known malware
- **Threat intelligence management** — dynamic keyword library simulating IOC (Indicator of Compromise) feeds
- **SOC triage workflows** — menu-driven interface modeling analyst decision points
- **Log-based threat detection** — behavioral analysis of authentication logs for anomalous patterns
- **Brute force detection** — frequency and time-window analysis of repeated login attempts

---

## Author

**Lateefat Alimi**  
BS Cybersecurity Operations | Minor in Data Analytics  
University of Nebraska at Kearney  
