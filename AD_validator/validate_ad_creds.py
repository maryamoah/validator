#!/usr/bin/env python3
"""
Simple Active Directory Credential Checker
------------------------------------------

This script verifies whether a provided username + password
successfully authenticate against Active Directory using NTLM.

Usage:
    python validate_ad_creds.py <email_or_username> <password>

Environment:
    AD_SERVER   → e.g. "dc01.example.com"
    AD_DOMAIN   → e.g. "EXAMPLE"
"""

from ldap3 import Server, Connection, NTLM, ALL
import os
import sys

# -------------------------------
# Configuration (safe for GitHub)
# -------------------------------
AD_SERVER = os.getenv("AD_SERVER")
AD_DOMAIN = os.getenv("AD_DOMAIN")


def normalise_username(user: str) -> str:
    """
    Accepts:
      - email (user@example.com)
      - username
      - DOMAIN\username
    Returns:
      DOMAIN\username in NTLM format
    """
    user = user.strip()

    if "\\" in user:
        return user  # already DOMAIN\username

    if "@" in user:
        user = user.split("@")[0]  # convert email → username

    return f"{AD_DOMAIN}\\{user}"


def validate_creds(user: str, password: str) -> bool:
    full_user = normalise_username(user)

    server = Server(AD_SERVER, get_info=ALL)

    try:
        conn = Connection(
            server,
            user=full_user,
            password=password,
            authentication=NTLM,
            raise_exceptions=True
        )

        return conn.bind()

    except Exception:
        return False


def main():
    if len(sys.argv) != 3:
        print("Usage: python validate_ad_creds.py <email_or_username> <password>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]

    print(f"[INFO] Testing credentials for: {user}")

    if validate_creds(user, password):
        print("[RESULT] ✅ VALID CREDS (Correct username + password)")
    else:
        print("[RESULT] ❌ INVALID CREDS (User not found OR wrong password)")


if __name__ == "__main__":
    main()
