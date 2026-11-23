# 🐛 Python Bug Hunt

A terminal-based classroom game that helps students practise identifying and fixing common Python errors.

## Features

- 20 debugging challenges across **Easy**, **Medium**, and **Hard** levels.
- Covers variables, input, operators, conditionals, loops, strings, lists, `break`, and `continue`.
- Supports 1–4 teams.
- Scoring for identifying the faulty line and error type.
- 30-second speed bonus, streak bonus, hints, and steal opportunities.
- Shows the explanation and suggested fix after each challenge.
- Uses only Python's standard library.

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run the game

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python bug_hunt.py
   ```

   On some systems, use:

   ```bash
   python3 bug_hunt.py
   ```

4. Enter the number of teams, team names, and number of rounds.
5. Take turns finding the bug!

## How to play

| Action | Points |
|---|---:|
| Identify a correct buggy line | +10 |
| Identify the correct error type | +5 |
| Answer within 30 seconds | +3 |
| Get 3 correct answers in a row | +5 |
| Use a hint | -3 |
| Successfully steal an answer | +5 |

Error types:
- **Syntax** — Python cannot parse the code.
- **Runtime** — the program starts but raises an exception while running.
- **Logic** — the program runs but produces an incorrect result.

## Project structure

```text
bug_hunt_github/
├── bug_hunt.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── tests/
    └── test_challenges.py
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Contributing

Suggestions for new challenges, improvements, and bug reports are welcome. Keep challenges beginner-friendly, include a hint, explanation, and corrected code, and test changes before submitting a pull request.

## License

This project is available under the MIT License. See [LICENSE](LICENSE).
