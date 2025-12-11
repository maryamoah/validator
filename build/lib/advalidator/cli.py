from .validator import validate_creds

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate Active Directory credentials.")
    parser.add_argument("--user", required=True, help="Username or email")
    parser.add_argument("--password", required=True, help="Password")

    args = parser.parse_args()

    print(f"[INFO] Testing credentials for: {args.user}")

    if validate_creds(args.user, args.password):
        print("[RESULT] ✅ VALID CREDS (Correct username + password)")
    else:
        print("[RESULT] ❌ INVALID CREDS (User not found OR wrong password)")
