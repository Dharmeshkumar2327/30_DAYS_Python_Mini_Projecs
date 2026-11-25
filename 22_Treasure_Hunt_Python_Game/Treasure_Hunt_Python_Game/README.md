# Treasure Hunt – Python Console Game

A beginner-friendly command-line treasure hunt game built with core Python concepts. A pirate's treasure is hidden at a random position on a 6 × 6 island. The player has up to seven valid digs to find it.

## Features

- Randomly hides the treasure on a 6 × 6 grid.
- Accepts row and column guesses from the player.
- Gives **HOT**, **WARM**, or **COLD** distance hints.
- Provides directional hints (up, down, left, right).
- Validates numeric input and grid boundaries.
- Calculates a score based on the number of digs used.
- Tracks wins and games played; supports replay.

## Project Structure

```text
Treasure_Hunt_Python_Game/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

- Python 3.8 or later
- No third-party packages are required. The game uses Python's built-in `random` module.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use:

   ```bash
   python3 main.py
   ```

4. Enter your pirate name and follow the prompts to guess the treasure's row and column.

## How to Play

1. The game hides treasure at a random row and column between 1 and 6.
2. Enter a row and a column for each dig.
3. Read the distance and direction hints.
4. Find the treasure within seven valid digs to win.
5. Choose `y` to play another round or `n` to exit.

Invalid entries do not use a dig.

## Python Concepts Demonstrated

- Variables and data types
- `input()` and type conversion with `int()`
- Conditional statements (`if`, `elif`, `else`)
- `while` and nested `for` loops
- Functions and return values
- The `random` module
- `abs()` and arithmetic operations
- Basic input validation

## Author

Add your name and GitHub profile here.
