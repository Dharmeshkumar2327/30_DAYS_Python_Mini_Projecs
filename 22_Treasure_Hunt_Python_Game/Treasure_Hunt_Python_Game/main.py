# ==========================================================
# TREASURE HUNT - A Python game using basics and loops
# Concepts: variables, input(), int(), if/elif/else,
#           while loop, nested for loops, random, abs()
# ==========================================================

import random


def draw_map(size, last_row, last_col):
    """Display the island map and mark the player's latest dig."""
    print("\n    ", end="")
    for column in range(1, size + 1):
        print(column, end="  ")
    print()

    for row in range(1, size + 1):
        print(" ", row, end=" ")
        for column in range(1, size + 1):
            if row == last_row and column == last_col:
                print("X", end="  ")
            else:
                print("~", end="  ")
        print()


def play_game(player):
    """Run one round of the treasure hunt."""
    size = 6
    max_digs = 7

    treasure_row = random.randint(1, size)
    treasure_col = random.randint(1, size)

    last_row = 0
    last_col = 0
    digs = 0
    found = False

    while digs < max_digs and not found:
        draw_map(size, last_row, last_col)
        print("\nDigs left:", max_digs - digs)

        row_text = input("Row (1-6): ")
        col_text = input("Column (1-6): ")

        if not row_text.isdigit() or not col_text.isdigit():
            print("Please type numbers only!")
            continue

        row = int(row_text)
        col = int(col_text)

        if row < 1 or row > size or col < 1 or col > size:
            print("That's in the sea! Choose between 1 and", size)
            continue

        digs += 1
        last_row = row
        last_col = col

        distance = abs(row - treasure_row) + abs(col - treasure_col)

        if distance == 0:
            found = True
        elif distance == 1:
            print("HOT! You are right next to it!")
        elif distance <= 3:
            print("WARM... getting closer.")
        else:
            print("COLD. Far away.")

        if distance != 0:
            if row < treasure_row:
                print("Hint: try going DOWN.")
            elif row > treasure_row:
                print("Hint: try going UP.")

            if col < treasure_col:
                print("Hint: try going RIGHT.")
            elif col > treasure_col:
                print("Hint: try going LEFT.")

    if found:
        score = (max_digs - digs + 1) * 10
        print("\n" + "*" * 45)
        print("  YO HO HO,", player + "! You found the treasure!")
        print("  Digs used:", digs, "  Score:", score)
        print("*" * 45)
        return True

    print(
        "Out of digs! The treasure was at row",
        treasure_row,
        "column",
        treasure_col
    )
    return False


def main():
    print("=" * 45)
    print("        WELCOME TO THE TREASURE HUNT!")
    print("=" * 45)
    print("A pirate has buried treasure on a 6 x 6 island.")
    print("Guess the ROW and COLUMN (1 to 6) to dig.")
    print("After every dig you get a hint: HOT, WARM or COLD.")
    print("Find it in 7 digs or less to win!\n")

    player = input("Enter your pirate name: ")
    play_again = "y"
    total_wins = 0
    games_played = 0

    while play_again == "y":
        games_played += 1
        if play_game(player):
            total_wins += 1

        play_again = input("\nPlay again? (y/n): ").lower()

    print("\nThanks for playing,", player + "!")
    print("You won", total_wins, "out of", games_played, "games.")


if __name__ == "__main__":
    main()
