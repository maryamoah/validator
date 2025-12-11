<p align="center">
  <img src="assets/logo-dark.svg" width="450">
</p>

# AD Credential Validator

![CI](https://github.com/maryamoah/validator/actions/workflows/python-app.yml/badge.svg)

A lightweight toolkit for validating Microsoft Active Directory (AD) credentials via NTLM.  
Designed for SOC automation pipelines, credential leak validation, and identity security tools.

---

## 🔧 Features

- NTLM authentication (no service account required)
- Validates `user@domain` or `username` formats
- Returns clean `True/False` results
- Production-ready structure for PyPI publishing

---

## 📦 Installation

```
pip install advalidator
```

---

## 🚀 Usage Example

```python
from advalidator import ADCredentialValidator

v = ADCredentialValidator(
    domain_controller="dc.example.com",
    domain="EXAMPLE"
)

if v.validate("jdoe", "Secret123"):
    print("✔ Valid credentials")
else:
    print("❌ Invalid")
```

---

## 📁 Project Structure

```
advalidator/
    validator.py
tests/
README.md
pyproject.toml
requirements.txt
```

---

## 📝 License
MIT
