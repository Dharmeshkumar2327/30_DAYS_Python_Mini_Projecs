# 🔐 Password Strength Checker

A simple command-line Python tool that checks how strong a password is and gives tips to make it stronger.

## Features

- Checks for **length**, **lowercase**, **uppercase**, **numbers** and **symbols**
- Rates passwords as **Weak**, **Medium** or **Strong** with a score out of 6
- Bonus point for long passwords (12+ characters)
- Rejects very **common passwords** (like `password123`)
- Warns about spaces in passwords
- Option to **hide the password** while typing
- Gives clear **suggestions** for improvement
- Includes unit tests

## How It Works

| Check | Points |
|-------|--------|
| At least 8 characters | 1 |
| Has lowercase letter | 1 |
| Has uppercase letter | 1 |
| Has a number | 1 |
| Has a symbol | 1 |
| 12+ characters (bonus) | 1 |

| Score | Rating |
|-------|--------|
| 0 – 2 | Weak |
| 3 – 4 | Medium |
| 5 – 6 | Strong |

## Getting Started

**Requirements:** Python 3.7+ (no external libraries needed)

```bash
git clone https://github.com/Dharmeshkumar2327/password-strength-checker.git
cd password-strength-checker
python password_checker.py
```

## Sample Output

```
========================================
       PASSWORD STRENGTH CHECKER
========================================

Show password while typing? (y/n): y
Enter password: hello2024

----------------------------------------
  [OK] At least 8 characters
  [OK] Lowercase letter
  [ X] Uppercase letter
  [OK] Number
  [ X] Symbol

  Strength: [###...]  Medium  (3/6)

  Tips to improve:
   - Add uppercase letters (A-Z).
   - Add symbols like ! @ # $ %.
----------------------------------------
```

## Running Tests

```bash
python -m unittest test_password_checker.py -v
```

## Concepts Used

- Strings and string methods (`isupper`, `isdigit`, ...)
- Loops and conditionals
- Functions and dictionaries
- `any()` with generator expressions
- `string` and `getpass` modules
- Unit testing with `unittest`

## Future Improvements

- GUI version using Tkinter
- Check against a larger list of leaked passwords
- Strong password generator
- Estimate time to crack

## Author

**Dharmesh Kumar**
- GitHub: [@Dharmeshkumar2327](https://github.com/Dharmeshkumar2327)
- LinkedIn: [Dharmesh Kumar](https://www.linkedin.com/in/dharmesh-kumar-293a89235)

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE).
