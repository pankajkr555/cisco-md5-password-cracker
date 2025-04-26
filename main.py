
#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

try:
    from passlib.hash import md5_crypt
    backend = "passlib"
except ImportError:
    md5_crypt = None
    try:
        import crypt
        backend = "crypt"
    except ImportError:
        backend = None

if not backend:
    sys.exit("No MD5-CRYPT backend available. Install passlib or use a Unix system.")

def check_password(pwd: str, h: str, salt: str) -> bool:
    if backend == "passlib":
        return md5_crypt.hash(pwd, salt=salt) == h
    return crypt.crypt(pwd, f"$1${salt}$") == h

def crack(h: str, wordlist: Path) -> str | None:
    _, _, salt, _ = h.split("$", 3)
    with wordlist.open("r", errors="ignore") as f:
        for i, line in enumerate(f, 1):
            pwd = line.rstrip("\n\r")
            if check_password(pwd, h, salt):
                print(f"Match after {i} tries -> '{pwd}'")
                return pwd
            if i % 100_000 == 0:
                print(f"{i:,} tested...", file=sys.stderr)
    return None

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-H", "--hash", required=True)
    ap.add_argument("-w", "--wordlist", type=Path, required=True)
    args = ap.parse_args()

    if not args.wordlist.exists():
        sys.exit(f"Wordlist not found: {args.wordlist}")

    print(f"Using backend: {backend}")
    pwd = crack(args.hash, args.wordlist)
    if pwd:
        print(f"Plaintext password: {pwd}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
