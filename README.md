# LogHunter 🔍

**CLI log parser for Apache, SSH, and Windows security logs – detect attacks, summarize threats. Optimized for Kali Linux.**

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Kali Linux](https://img.shields.io/badge/Kali-Linux-blue)



## 🎯 Purpose
LogHunter helps blue teams and SOC analysts quickly identify:
- Top attacking IPs
- Failed login patterns over time
- User enumeration attempts
- Directory traversal (Apache)



## 📦 Installation (Kali Linux)

```bash
# Clone the Repository
git clone https://github.com/alitalhahere/LogHunter.git

# Move to the Project Directory
cd LogHunter

# Enable Python Environment
python3 -m venv venv
source venv/bin/activate

# Install Requirements
pip install -r requirements.txt
```


## 🚀 Usage on Kali

```bash
# SSH logs (real-time from Kali)
sudo python -m loghunter.cli --type ssh --file /var/log/auth.log

# Apache logs (if Apache is running)
sudo python -m loghunter.cli --type apache --file /var/log/apache2/access.log

# Sample files (for testing)
python -m loghunter.cli --type apache --file samples/apache_access.log
```


## 🧪 Generate Real Attack Traffic on Kali

```bash
# Simulate SSH brute force
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1 -t 4

# Then run LogHunter on /var/log/auth.log
```


## 🛣️ Roadmap

- GeoIP lookup for attacker locations

- Real-time tail mode (-f flag)

- JSON output for SIEM integration



## 🤝 Contributing

Welcome to the Pull requests.



## 👤 Author

Ali Talha 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-connect-blue)](https://www.linkedin.com/in/imalitalha)
