#!/usr/bin/env python3
import sys
import os
from ldap3 import Server, Connection, NTLM, ALL

# --------------------------------------------------
# Load configuration from environment variables ONLY
# --------------------------------------------------
AD_SERVER = os.getenv("AD_SERVER")    # e.g. "dc01.example.com"
AD_DOMAIN = os.getenv("AD_DOMAIN")    # e.g. "MYORG"

if not AD_SERVER or not AD_DOMAIN:
    print("[ERROR] Missing AD_SERVER or AD_DOMAIN environment variables.")
    print("        Set them before running:")
    print("        export AD_SERVER=dc01.example.com")
    print("        export AD_DOMAIN=MYORG")
    sys.exit(1)


def normalize_username(username: str) -> str:
    """Convert email → DOMAIN\\username."""
    if "@" in username:
        username = username.split("@")[0]
    return f"{AD_DOMAIN}\\{username}"


def validate_creds(username: str, password: str) -> bool:
    """Validate one credential pair against Active Directory."""
    full_user = normalize_username(username)

    try:
        server = Server(AD_SERVER, get_info=ALL)
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


def load_from_file(path: str):
    """Load credentials from a file: 'user pass' per line."""
    creds = []
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    creds.append((parts[0], parts[1]))
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
    return creds


def parse_args(argv):
    """Interpret CLI arguments."""
    if len(argv) == 2:
        return load_from_file(argv[1])

    creds = []
    for pair in argv[1:]:
        if ":" not in pair:
            print(f"[WARN] Skipping invalid entry: {pair}")
            continue
        user, pwd = pair.split(":", 1)
        creds.append((user, pwd))

    return creds


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python validate_ad_creds.py user:pass user2:pass2 ...")
        print("  python validate_ad_creds.py creds.txt   # file mode")
        return

    creds = parse_args(sys.argv)

    print(f"[INFO] Loaded {len(creds)} credentials\n")

    for user, pwd in creds:
        print(f"[CHECK] {user} ... ", end="")
        if validate_creds(user, pwd):
            print("✅ VALID")
        else:
            print("❌ INVALID")


if __name__ == "__main__":
    main()
