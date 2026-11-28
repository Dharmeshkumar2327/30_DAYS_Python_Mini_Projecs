"""
Password Strength Checker
-------------------------
Checks a password against common security rules and rates it as
Weak, Medium or Strong, with tips on how to improve it.

Author: Dharmesh Kumar
"""

import getpass
import string

MIN_LENGTH = 8
STRONG_LENGTH = 12

# A few very common passwords that should always be rejected
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty", "abc123",
    "111111", "iloveyou", "admin", "welcome", "letmein", "password123",
}


def check_password(password):
    """Return a dict with the score, rating and list of suggestions."""
    checks = {
        "length": len(password) >= MIN_LENGTH,
        "lowercase": any(ch.islower() for ch in password),
        "uppercase": any(ch.isupper() for ch in password),
        "digit": any(ch.isdigit() for ch in password),
        "symbol": any(ch in string.punctuation for ch in password),
    }

    suggestions = []
    if not checks["length"]:
        suggestions.append(f"Use at least {MIN_LENGTH} characters.")
    if not checks["lowercase"]:
        suggestions.append("Add lowercase letters (a-z).")
    if not checks["uppercase"]:
        suggestions.append("Add uppercase letters (A-Z).")
    if not checks["digit"]:
        suggestions.append("Add numbers (0-9).")
    if not checks["symbol"]:
        suggestions.append("Add symbols like ! @ # $ %.")
    if " " in password:
        suggestions.append("Avoid spaces in your password.")

    score = sum(checks.values())          # 0 to 5
    if len(password) >= STRONG_LENGTH:
        score += 1                         # bonus point for long passwords

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.insert(0, "This is a very common password - choose another.")

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return {"score": score, "rating": rating, "checks": checks,
            "suggestions": suggestions}


def show_result(result):
    """Print the result in a friendly format."""
    print("\n" + "-" * 40)
    labels = {
        "length": f"At least {MIN_LENGTH} characters",
        "lowercase": "Lowercase letter",
        "uppercase": "Uppercase letter",
        "digit": "Number",
        "symbol": "Symbol",
    }
    for key, label in labels.items():
        mark = "[OK]" if result["checks"][key] else "[ X]"
        print(f"  {mark} {label}")

    bar = "#" * result["score"] + "." * (6 - result["score"])
    print(f"\n  Strength: [{bar}]  {result['rating']}  ({result['score']}/6)")

    if result["suggestions"]:
        print("\n  Tips to improve:")
        for tip in result["suggestions"]:
            print(f"   - {tip}")
    else:
        print("\n  Great password!")
    print("-" * 40)


def main():
    print("=" * 40)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    while True:
        choice = input("\nShow password while typing? (y/n): ").strip().lower()
        if choice == "y":
            password = input("Enter password: ")
        else:
            password = getpass.getpass("Enter password (hidden): ")

        if not password:
            print("Password cannot be empty.")
            continue

        show_result(check_password(password))

        again = input("\nCheck another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay secure.")
            break


if __name__ == "__main__":
    main()
