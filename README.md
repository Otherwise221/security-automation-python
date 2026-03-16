# security-automation-python
## Independent Study Project -- Jan - May 2026 -- UNK

# File Analysis & Malicious Indicator Detection Tool

A Python-based security automation tool built for static file analysis. This tool simulates core triage workflows used in SOC environments — scanning files for malicious indicators, generating and comparing file hashes, and managing a dynamic threat keyword library.

---

## Background

This project was developed as part of an independent study in Python Security Automation. The goal was to build a practical, menu-driven tool that automates common malware triage tasks — reducing manual analysis time and improving consistency in threat detection.

---

## Features

| Option | Function |
|--------|----------|
| A | Scan a file for malicious indicator keywords |
| B | Generate a SHA-256 hash of a file and store it in the hash library |
| E | Add a new keyword to the malicious indicator list |
| G | Compare a file's hash against the stored hash library |
| Z | Quit |

> Options C (Suspicious Patterns) and D (Behavioral Signatures) are in active development.

---

## How It Works

### Malicious Indicator Scanning
The tool reads a target file line by line and checks each line against a customizable keyword list (`Keywords.txt`). Keywords represent known malicious indicators such as tool names, suspicious executables, and attacker techniques. Matches are reported with the line number, keyword found, and the full line content.

**Sample keywords include:**
`mimikatz`, `rundll32`, `mshta`, `wscript`, `powershell.exe`, `keylogger`, `rootkit`, `payload`, `tor`, `exfil`

### Hash Generation & Comparison
Files are hashed using **SHA-256** via Python's `hashlib` module. Generated hashes are stored in `hashLibrary.txt`. The comparison feature checks whether a given file's hash matches any stored hash — useful for identifying known malicious files or verifying file integrity.

### Dynamic Keyword Management
Users can add new malicious indicators to the keyword list at runtime. Duplicate detection prevents redundant entries. This simulates how threat intelligence feeds update detection rules in real SOC environments.

---

## File Structure

```
├── Analysis.py              # Main tool — menu-driven interface
├── Malicious_Indicators.py  # Early prototype of the indicator scanner
├── keyword_maker.py         # Standalone keyword management utility
├── Keywords.txt             # Malicious indicator keyword library
├── hashLibrary.txt          # Stored SHA-256 file hashes
└── file.txt                 # Sample test file
```

---

## Getting Started

**Requirements:** Python 3.x (no external libraries needed)

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/security-automation-python.git
cd security-automation-python

# Run the tool
python Analysis.py
```

---

## Security Concepts Demonstrated

- **Static file analysis** — scanning file contents against known threat indicators
- **File integrity checking** — SHA-256 hashing to detect file tampering or known malware
- **Threat intelligence management** — dynamic keyword library simulating IOC (Indicator of Compromise) feeds
- **SOC triage workflows** — menu-driven interface modeling analyst decision points

---

## Roadmap

- [ ] Complete keyword deletion functionality
- [ ] Implement suspicious pattern detection (Option C)
- [ ] Implement behavioral signature analysis (Option D)
- [ ] Add directory scanning (scan all files in a folder)
- [ ] Export scan results to a report file

---

## Author

**Lateefat Alimi**  
BS Cybersecurity Operations | Minor in Data Analytics  
University of Nebraska at Kearney  
