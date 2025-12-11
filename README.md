
# 🔐 AD Credential Validator

A lightweight Python tool for validating **Active Directory username + password** pairs using NTLM authentication.  
This tool is ideal for SOC teams, security investigations, leak verification, and incident response workflows.

---

## 🚀 Features

- ✔️ Validates AD credentials using NTLM  
- ✔️ Accepts both `email@example.com` and `DOMAIN\username` formats  
- ✔️ No service account required  
- ✔️ CLI-based and automation-friendly  
- ✔️ Minimal dependencies  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/maryamoah/validator.git
cd validator
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

Run the script as follows:

```bash
python validate_ad_creds.py <email_or_username> <password>
```

### Examples:

```bash
python validate_ad_creds.py user@example.com "StrongPass123"
python validate_ad_creds.py DOMAIN\username "Password123!"
```

---

## 📝 Example Output

### **Valid credentials**

```
[INFO] Validating: user@example.com
[RESULT] ✅ VALID CREDS (User + Password are correct)
```

### **Invalid credentials**

```
[INFO] Validating: user@example.com
[RESULT] ❌ INVALID (User not found OR password incorrect)
```

---

## ⚙️ Configuration

Modify the Domain Controller address in the script:

```python
AD_SERVER = "your.domain.controller"
```

Ensure your system can reach the controller over the network.

---

## ⚠️ Security Notes

- Credentials are used only for immediate verification and **never stored**  
- Does not perform brute-force, enumeration, or password spraying  
- Intended solely for defensive purposes  

---

## 📄 License

MIT License — free to use, modify, and integrate.

---

## 🛡️ Disclaimer

Use responsibly and only on systems you are authorized to test.
