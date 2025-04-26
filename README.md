# cisco-md5-password-cracker
🛡️ A Python script to crack Cisco Type 5 MD5-CRYPT password hashes using a wordlist. Learn ethical hacking the right way!

# 🔐 Cisco MD5 Password Cracker (Type 5)

A Python script to crack Cisco Type 5 MD5-CRYPT password hashes using a wordlist like rockyou.txt.

## 💡 Features

- Detects MD5-crypt password format  
- Cracks password using dictionary attack  
- Uses `passlib` or `crypt` backend  
- Command-line arguments for hash and wordlist  
- Clean and educational code for learning  

## 🛠️ Requirements

```bash
pip install passlib

🚀 Usage

python3 md5cracker.py -H '$1$salt$hashvalue' -w rockyou.txt

📥 Sample Cisco Hash Format

username admin password 5 $1$DfGh$yfsr1kkaksJXflfdTnsdL/

📂 Download rockyou.txt Wordlist

The famous rockyou.txt wordlist contains millions of passwords and is useful for password cracking tasks.

🔗 Download from GitHub
👉 https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

📦 After downloading:

mv rockyou.txt /your/path/here/

Or use:

wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

Make sure your Python script and wordlist file are in the same folder.

🎯 Output

Match after 2633 tries -> 'admin123'
Plaintext password: admin123

📚 Blog Tutorial

👉 Read Full Blog in English + Hindi
📌 Coming soon on cybermentor33.com
🔐 For Educational Purposes Only

This tool is intended for cybersecurity learning, auditing, and ethical hacking practices only.

Author: @pankajkumar 💻
