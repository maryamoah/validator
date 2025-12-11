
# 🌐 AD Validator

```
     _    ____      __     _       _ _           
    / \  |  _ \ ___/ _|   / \   __| (_) ___ _ __ 
   / _ \ | | | / _ \ |_   / _ \ / _` | |/ _ \ '__|
  / ___ \| |_| |  __/  _| / ___ \ (_| | |  __/ |   
 /_/   \_\____/ \___|_|  /_/   \_\__,_|_|\___|_|   

         Simple • Secure • Fast • NTLM Validator
```

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.8+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Auth-NTLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/CLI-validate--creds-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success?style=for-the-badge">
</p>

---

## 🛡️ Overview

**AD Validator** is a lightweight CLI tool for validating Active Directory credentials.  
Designed for SOC teams, automation pipelines, pentesting labs, and security engineers.

```
       +-------------------+
       |   User Inputs     |
       |  (user/pass)      |
       +---------+---------+
                 |
                 v
     +-----------+-----------+
     |  AD Validator (CLI)   |
     | validate-creds 🛠️     |
     +-----------+-----------+
                 |
                 v
   +-------------+--------------+
   | Active Directory (NTLM) 🏢 |
   +-------------+--------------+
                 |
                 v
        +--------+--------+
        |   Result ✔/❌    |
        +------------------+
```

---

## ✨ Features

- 🔐 Single or bulk credential validation  
- 📁 File‑based or inline input  
- 🌍 Supports email, username, or `DOMAIN\user`  
- ⚙️ Uses only environment variables  
- 🧪 Ideal for SOC automation workflows  
- 🚀 Packaged CLI tool: `validate-creds`

---

## 📦 Installation

```bash
git clone https://github.com/maryamoah/validator.git
cd validator
pip install .
```

Reinstall cleanly:

```bash
pip install --force-reinstall .
```

---

## 🔧 Environment Variables

Set these **before running**:

### Windows (PowerShell)

```powershell
setx AD_SERVER "dc01.example.com"
setx AD_DOMAIN "MYORG"
```

### Linux / macOS

```bash
export AD_SERVER="dc01.example.com"
export AD_DOMAIN="MYORG"
```

> 🔁 Restart your terminal afterward.

---

## 🚀 Usage Examples

### **1️⃣ Validate one credential**
```bash
validate-creds --user alice --password Pass123
```

### **2️⃣ Multiple inline credentials**
```bash
validate-creds alice:Pass123 bob:WrongPwd admin:Summer2025!
```

### **3️⃣ Validate from file**
`creds.txt`:
```
alice Pass123
bob WrongPwd
charlie Testing2025!
```

Run:
```bash
validate-creds creds.txt
```

---

## 🧪 Testing

```bash
pip show advalidator
python -m advalidator.cli --user test --password test
```

Python import test:
```python
from advalidator.validator import validate_creds
print(validate_creds("alice", "Pass123"))
```

---

## 📂 Project Structure

```
validator/
│── advalidator/
│     ├── __init__.py
│     ├── cli.py
│     └── validator.py
│── README.md
│── pyproject.toml
│── requirements.txt
```

---

## 🔐 Security Notes

- ❌ No credential storage  
- ❌ No logging of passwords  
- ✔ Direct NTLM auth via ldap3  
- ✔ Intended for legitimate, authorized environments  

---

## 🛠️ Future Enhancements

- LDAPS support  
- Password complexity analysis  
- GitHub Actions CI  
- Docker image  
- PyPI release  

---

## 👤 Author

**Mary Amoah**  
Security Operations & Automation Engineer  

🌟 *Built for real SOC workflows.*  
