# OBNTATHLOS
OSINT Collection Tool is a Python-based tool for automated OSINT gathering. It includes modules for WHOIS lookups, IP geolocation, DNS resolution, directory fuzzing, document finding, Google dorking, and email scraping. Ideal for cybersecurity professionals and penetration testers to quickly gather valuable information.

# 🕵️‍♂️ OSINT Collection Tool

**OSINT Collection Tool** is a user-friendly, Python-based application designed for automated Open Source Intelligence (OSINT) gathering. With a simple menu-driven interface, cybersecurity professionals and penetration testers can perform critical reconnaissance tasks with just a few key presses.

---

![image](https://github.com/user-attachments/assets/304eff0e-d7f2-4cd9-9c9f-dbe6ab6cb8d2)


## ✅ Features

🔍 **WHOIS Lookup**  
🌐 **IP Geolocation**  
🧠 **DNS Resolution**  
📁 **Directory Fuzzing**  
📄 **Document Finder**  
🕸️ **Google Dorking**  
📧 **Email Scraper**

---

## 🎯 Use Case

This tool is ideal for:
- Bug bounty hunters
- Ethical hackers
- SOC analysts
- Red teamers
- Security researchers

---
#installation
```
sudo git clone https://github.com/Ajay-Bommidi/OBNTATHLOS.git
cd OBNTATHLOS
sudo python3 -m venv myenv
source myenv/bin/activate
sudo chown -R $USER:$USER ~/OBNTATHLOS/myenv
pip install -r requirements.txt
sudo python OBNTATHLOS.py
```

## 🚀 How to Use

1. **Run the script**  
2. **Choose a number from the menu**  
3. **Enter the required input (domain/IP/email/etc.)**  
4. **View the results instantly!**

🧭 **Example:**
[1] WHOIS Lookup

[2] IP Geolocation

[3] DNS Resolver

[4] Directory Fuzzing

[5] Document Finder

[6] Google Dorking

[7] Email Scraper

[0] Exit

Select an option: 2
Enter IP Address: 93.184.216.34
🛠️ Requirements
Python 3.7+

Modules:

requests
bs4
socket
dns.resolver
ipwhois
python-whois
re, os, subprocess
(Use pip install -r requirements.txt if a file is included.)

📦 Modules Overview

| Module                | Description                               |
| --------------------- | ----------------------------------------- |
| **WHOIS Lookup**      | Extracts domain registration data         |
| **IP Geolocation**    | Fetches geolocation of an IP address      |
| **DNS Resolver**      | Finds A, MX, TXT, NS records              |
| **Directory Fuzzing** | Bruteforces directories on a web server   |
| **Document Finder**   | Searches for files like `.pdf`, `.docx`   |
| **Google Dorking**    | Uses dorks to find indexed sensitive data |
| **Email Scraper**     | Scrapes emails from websites              |

⚠️ Disclaimer
This tool is for educational and authorized security testing only. Unauthorized usage against systems you don’t own or have permission to test is illegal.

📚 License
MIT License © 2025 – Ajay Bommidi
