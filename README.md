# 🔐 AD Credential Validator

A lightweight Python tool to **validate Active Directory username + password pairs** using LDAP/NTLM — ideal for quickly checking whether leaked or suspected credentials are actually valid in your environment.

---

## 🌟 What this tool does

- ✅ Verifies if a **username + password** combination is valid against an AD Domain Controller  
- 🧾 Accepts both `user@example.com` and `DOMAIN\\username` formats  
- 🔄 Automatically normalizes email-style usernames into `DOMAIN\\username`  
- 🧪 Designed for **manual triage** and **scripted checks** (e.g., against leaked credential lists)  
- 🪶 Minimal dependencies, built on top of [`ldap3`](https://ldap3.readthedocs.io/)  

> ⚠️ **Important:** This tool does **not** brute-force or spray passwords.  
> It only validates credentials you already have (e.g., from incident response or leak analysis).

---

## 🧱 Project Structure

```bash
validator/
├── AD_validator/
│   └── validate_ad_creds.py     # Main script: validates a single username+password pair
├── requirements.txt             # Python dependencies (ldap3)
└── README.md                    # This documentation
```

---

## 🛠️ Requirements

- Python **3.9+** (3.10 / 3.11 recommended)
- Network connectivity to your **Active Directory Domain Controller**
- The `ldap3` library (installed via `requirements.txt`)

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/validator.git
cd validator
pip install -r requirements.txt
```

> On Windows you may need to use `py -m pip install -r requirements.txt`.

---

## ⚙️ Configuration

Edit the following constant in `AD_validator/validate_ad_creds.py`:

```python
AD_SERVER = "dc1.example.local"   # Replace with your domain controller FQDN or IP
```

The tool assumes:

- Your AD domain is something like `EXAMPLE.LOCAL`
- Your NTLM login format is: `EXAMPLE\\username`

If your domain name is different, simply update:

```python
full_user = f"EXAMPLE\\{username}"
```

to match your environment’s domain (e.g., `COMPANY`, `CORP`, etc.).

---

## ▶️ Usage

From the project root:

```bash
cd AD_validator
python validate_ad_creds.py <username_or_email> <password>
```

### Example 1 — Email-style username

```bash
python validate_ad_creds.py alice@example.com MySecretPassword123
```

**Output (valid):**

```text
[INFO] Validating: alice@example.com
[RESULT] ✅ VALID CREDS (User + Password are correct)
```

**Output (invalid):**

```text
[INFO] Validating: alice@example.com
[RESULT] ❌ INVALID (User not found OR password incorrect)
```

---

### Example 2 — DOMAIN\\username format

```bash
python validate_ad_creds.py "EXAMPLE\\alice" MySecretPassword123
```

> If you pass `EXAMPLE\\alice`, the script will use it directly and skip email normalization.

---

## 🔍 How it works (internals)

The script:

1. Normalizes the username  
2. Attempts an **NTLM bind** to the specified `AD_SERVER`  
3. Returns:
   - `True` if bind succeeds → credentials are valid  
   - `False` if bind fails → user doesn’t exist or password is wrong  

No passwords are stored or logged beyond the process’ lifetime.

---

## 🧪 Common usage scenarios

- 🔐 **Leak validation**  
  You have username + password from an external dump and want to check if they still work internally.

- 🕵️ **IR / DFIR triage**  
  During incident response, quickly check whether reported credentials are real or fabricated.

- 🔄 **Pipeline integration**  
  Wrap this script in:
  - SIEM/SOAR playbooks  
  - n8n, Node-RED, Airflow, or custom automation flows  
  - Python scripts that read from CSV / JSON lists of credentials  

---

## ⚠️ Security & Ethical Notes

- Only use this on **accounts you are legally allowed to test** (your own organization).  
- Test credentials over secure internal networks whenever possible.  
- Consider logging validation attempts securely for audit purposes.  
- Do **not** integrate this into high-frequency password spraying tools — that would likely violate policy and law.

---

## 🚀 Ideas for Extension

Some potential next steps you (or contributors) could implement:

- ✅ Read username/password pairs from a CSV file and batch-validate  
- ✅ Export results (valid/invalid) as JSON/CSV for ingestion by SIEM  
- ✅ Add optional LDAP search to confirm user existence even if the password is wrong  
- ✅ Wrap as a small Flask API or FastAPI microservice for internal use  
- ✅ Add unit tests and publish to PyPI as a small utility package

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Commit changes: `git commit -m "Improve X"`
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and integrate it in your own internal tooling.

---

## ⭐ If this project helps you…

- Give the repository a **star** on GitHub  
- Share it with your blue team / SOC / IR colleagues  
- Open an issue or PR with improvements or ideas

