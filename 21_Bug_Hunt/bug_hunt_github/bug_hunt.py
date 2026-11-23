"""
BUG HUNT  -  A classroom Python debugging game
-----------------------------------------------
Topics covered: variables, input, operators, if/elif/else, for, while,
range, strings, simple lists, break/continue.

How to play:
  * 1-4 teams take turns. Each round shows a short buggy program.
  * Step 1: Spot the line with the bug           -> +10 points
  * Step 2: Name the bug type (Syntax/Runtime/Logic) -> +5 points
  * Answer within 30 seconds                     -> +3 speed bonus
  * 3 correct in a row                           -> +5 streak bonus
  * Type  h  for a hint (costs 3 points)
  * If a team misses, the next team can STEAL for +5.

Run:  python bug_hunt.py
"""

import os
import random
import time

os.system("")  # enables ANSI colours on Windows terminals

# ---------- colours ----------
R, G, Y, B, C, M, W, BOLD, END = (
    "\033[91m", "\033[92m", "\033[93m", "\033[94m",
    "\033[96m", "\033[95m", "\033[97m", "\033[1m", "\033[0m",
)

BUG_TYPES = {"1": "Syntax", "2": "Runtime", "3": "Logic"}

# ---------- challenge bank ----------
# lines: list of code lines | bug: acceptable line numbers | type: Syntax/Runtime/Logic
CHALLENGES = [
    # ----- EASY -----
    dict(level="Easy", title="Even or Odd",
         goal="Tell the user whether a number is even or odd.",
         happens="Python refuses to run the program at all.",
         lines=['num = int(input("Enter a number: "))',
                'if num % 2 = 0:',
                '    print("Even")',
                'else:',
                '    print("Odd")'],
         bug=[2], type="Syntax",
         hint="Are we assigning a value or comparing two values?",
         explain="'=' assigns a value; '==' compares. Inside an if, we need comparison.",
         fix='if num % 2 == 0:'),

    dict(level="Easy", title="The Missing Colon",
         goal="Print 'Big' if x is greater than 5.",
         happens="SyntaxError before anything runs.",
         lines=['x = 10',
                'if x > 5',
                '    print("Big")'],
         bug=[2], type="Syntax",
         hint="Every if, for, while and else line ends with a special character.",
         explain="if / elif / else / for / while lines must end with a colon ':'.",
         fix='if x > 5:'),

    dict(level="Easy", title="Lost Indentation",
         goal="Print 'Python' three times.",
         happens="IndentationError: expected an indented block.",
         lines=['for i in range(3):',
                'print("Python")'],
         bug=[2], type="Syntax",
         hint="How does Python know which lines belong inside the loop?",
         explain="The loop body must be indented (4 spaces) under the for line.",
         fix='    print("Python")'),

    dict(level="Easy", title="Unclosed Quote",
         goal="Print a welcome message.",
         happens="SyntaxError: unterminated string literal.",
         lines=['print("Welcome to Python)',
                'print("Let us begin!")'],
         bug=[1], type="Syntax",
         hint="Count the quotation marks on each line.",
         explain="A string that opens with \" must also close with \".",
         fix='print("Welcome to Python")'),

    dict(level="Easy", title="Who is Name?",
         goal="Greet the user by name.",
         happens="NameError: name 'Name' is not defined.",
         lines=['name = "Asha"',
                'print("Hello, " + Name)'],
         bug=[2], type="Runtime",
         hint="Python is case-sensitive. Look closely at the letters.",
         explain="'name' and 'Name' are two different variables in Python.",
         fix='print("Hello, " + name)'),

    dict(level="Easy", title="Birthday Maths",
         goal="Tell the user how old they will be next year.",
         happens="TypeError: can only concatenate str (not \"int\") to str.",
         lines=['age = input("Enter your age: ")',
                'next_age = age + 1',
                'print("Next year you will be", next_age)'],
         bug=[1, 2], type="Runtime",
         hint="What data type does input() always give back?",
         explain="input() returns a string. Convert it with int() before adding 1.",
         fix='age = int(input("Enter your age: "))'),

    dict(level="Easy", title="Divide by Nothing",
         goal="Find the average marks of students.",
         happens="ZeroDivisionError: division by zero.",
         lines=['total = 450',
                'count = 0',
                'average = total / count',
                'print("Average:", average)'],
         bug=[2, 3], type="Runtime",
         hint="What number can you never divide by?",
         explain="count is 0, and dividing by zero crashes the program.",
         fix='count = 5   # number of students'),

    # ----- MEDIUM -----
    dict(level="Medium", title="Almost Ten",
         goal="Add the numbers 1 to 10. Expected: 55",
         happens="Prints: Sum is 45",
         lines=['total = 0',
                'for i in range(1, 10):',
                '    total = total + i',
                'print("Sum is", total)'],
         bug=[2], type="Logic",
         hint="Does range(1, 10) include the number 10?",
         explain="range(start, stop) stops BEFORE 'stop'. Use range(1, 11).",
         fix='for i in range(1, 11):'),

    dict(level="Medium", title="Zero Factorial",
         goal="Find 5! (factorial). Expected: 120",
         happens="Prints: 0",
         lines=['n = 5',
                'fact = 0',
                'for i in range(1, n + 1):',
                '    fact = fact * i',
                'print(fact)'],
         bug=[2], type="Logic",
         hint="What is 0 multiplied by anything?",
         explain="Starting a product at 0 keeps it 0 forever. Start at 1.",
         fix='fact = 1'),

    dict(level="Medium", title="Wrong Table",
         goal="Print the 7 times table (7 x 1 = 7 ... 7 x 10 = 70).",
         happens="Every line shows 49.",
         lines=['n = 7',
                'for i in range(1, 11):',
                '    print(n, "x", i, "=", n * n)'],
         bug=[3], type="Logic",
         hint="Which variable should change on every line?",
         explain="We multiplied n by itself. It should be n * i.",
         fix='    print(n, "x", i, "=", n * i)'),

    dict(level="Medium", title="Vowel Counter",
         goal="Count vowels in 'education'. Expected: 5",
         happens="Prints: Vowels: 1",
         lines=['word = "education"',
                'count = 0',
                'for ch in word:',
                '    if ch in "aeiou":',
                '        count = 1',
                'print("Vowels:", count)'],
         bug=[5], type="Logic",
         hint="Is count being increased, or just reset?",
         explain="count = 1 resets it each time. Use count = count + 1.",
         fix='        count = count + 1'),

    dict(level="Medium", title="Average Gone Wrong",
         goal="Average of 10 and 20. Expected: 15.0",
         happens="Prints: Average: 20.0",
         lines=['a = 10',
                'b = 20',
                'avg = a + b / 2',
                'print("Average:", avg)'],
         bug=[3], type="Logic",
         hint="Which happens first in Python: + or / ?",
         explain="Division happens before addition (BODMAS). Use brackets.",
         fix='avg = (a + b) / 2'),

    dict(level="Medium", title="Unfair Grades",
         goal="85 marks should get 'Grade B'.",
         happens="Prints: Grade C",
         lines=['marks = 85',
                'if marks >= 50:',
                '    print("Grade C")',
                'elif marks >= 75:',
                '    print("Grade B")',
                'elif marks >= 90:',
                '    print("Grade A")'],
         bug=[2], type="Logic",
         hint="Python checks conditions top to bottom and stops at the first True.",
         explain="85 >= 50 is True first, so it never reaches the B check. "
                 "Check the highest grade first.",
         fix='if marks >= 90:  (then >= 75, then >= 50)'),

    dict(level="Medium", title="Smallest Biggest",
         goal="Find the biggest number in [4, 9, 2, 7]. Expected: 9",
         happens="Prints: 0",
         lines=['nums = [4, 9, 2, 7]',
                'biggest = 0',
                'for n in nums:',
                '    if n < biggest:',
                '        biggest = n',
                'print(biggest)'],
         bug=[4], type="Logic",
         hint="When should we replace 'biggest'?",
         explain="We should update when n is GREATER than biggest.",
         fix='    if n > biggest:'),

    # ----- HARD -----
    dict(level="Hard", title="Endless Countdown",
         goal="Print 5 4 3 2 1 then 'Blast off!'",
         happens="Prints 5 forever. The program never stops!",
         lines=['n = 5',
                'while n > 0:',
                '    print(n)',
                'print("Blast off!")'],
         bug=[2, 3], type="Logic",
         hint="Does n ever change inside the loop?",
         explain="n is never decreased, so 'n > 0' is always True: infinite loop.",
         fix='    print(n)\n      n = n - 1'),

    dict(level="Hard", title="Skip the Threes",
         goal="Print 1 to 10 but skip multiples of 3.",
         happens="Prints only: 1 2",
         lines=['for i in range(1, 11):',
                '    if i % 3 == 0:',
                '        break',
                '    print(i)'],
         bug=[3], type="Logic",
         hint="One keyword stops the loop, another just skips one turn.",
         explain="break exits the whole loop. continue skips only this turn.",
         fix='        continue'),

    dict(level="Hard", title="The Locked Door",
         goal="Keep asking for the password until it is 'python123'.",
         happens="Prints 'Access granted' without asking anything!",
         lines=['password = ""',
                'while password == "python123":',
                '    password = input("Enter password: ")',
                'print("Access granted")'],
         bug=[2], type="Logic",
         hint="The loop should continue while the password is WRONG.",
         explain="The loop runs only when the condition is True. '' == 'python123' "
                 "is False, so it never runs. Use !=",
         fix='while password != "python123":'),

    dict(level="Hard", title="Backwards Nothing",
         goal="Count down: 5 4 3 2 1 then 'Done'.",
         happens="Prints only: Done",
         lines=['for i in range(5, 0):',
                '    print(i)',
                'print("Done")'],
         bug=[1], type="Logic",
         hint="By default range() counts upward by +1.",
         explain="range(5, 0) is empty. To count down, add a step of -1.",
         fix='for i in range(5, 0, -1):'),

    dict(level="Hard", title="Letter by Letter",
         goal="Print each letter of 'loop' on its own line.",
         happens="Prints l o o p, then IndexError: string index out of range.",
         lines=['word = "loop"',
                'for i in range(len(word) + 1):',
                '    print(word[i])'],
         bug=[2, 3], type="Runtime",
         hint="'loop' has 4 letters. What are the valid index numbers?",
         explain="Valid indexes are 0 to len-1 (0-3). range(len(word)+1) goes to 4.",
         fix='for i in range(len(word)):'),

    dict(level="Hard", title="Digit Disaster",
         goal="Sum the digits of 1234. Expected: 10",
         happens="Prints a strange decimal like 11.1111...",
         lines=['n = 1234',
                'total = 0',
                'while n > 0:',
                '    total = total + n % 10',
                '    n = n / 10',
                'print(total)'],
         bug=[5], type="Logic",
         hint="What is 1234 / 10? What about 1234 // 10?",
         explain="'/' gives a decimal (123.4). '//' drops the decimal (123).",
         fix='    n = n // 10'),
]


# ---------- helpers ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"""{G}{BOLD}
   ____              _   _             _
  | __ ) _   _  __ _| | | |_   _ _ __ | |_
  |  _ \\| | | |/ _` | |_| | | | | '_ \\| __|
  | |_) | |_| | (_| |  _  | |_| | | | | |_
  |____/ \\__,_|\\__, |_| |_|\\__,_|_| |_|\\__|
               |___/      {Y}find the bug, win the round!{END}
""")


def show_code(ch):
    colour = {"Easy": G, "Medium": Y, "Hard": R}[ch["level"]]
    print(f"{colour}{BOLD}[{ch['level']}]{END} {BOLD}{ch['title']}{END}\n")
    print(f"  {C}Goal:{END}          {ch['goal']}")
    print(f"  {M}What happens:{END}  {ch['happens']}\n")
    print(f"  {B}{'-' * 48}{END}")
    for i, line in enumerate(ch["lines"], 1):
        print(f"  {B}{i:>2} |{END} {W}{line}{END}")
    print(f"  {B}{'-' * 48}{END}\n")


def ask_line(ch, prompt):
    """Return (line_number, used_hint)."""
    used_hint = False
    while True:
        ans = input(prompt).strip().lower()
        if ans == "h" and not used_hint:
            used_hint = True
            print(f"  {Y}Hint: {ch['hint']}{END}  (-3 points)\n")
            continue
        if ans.isdigit() and 1 <= int(ans) <= len(ch["lines"]):
            return int(ans), used_hint
        print(f"  Enter a line number 1-{len(ch['lines'])}" +
              ("" if used_hint else " or h for hint"))


def ask_type():
    while True:
        ans = input(f"  Bug type?  {G}1{END}=Syntax  {Y}2{END}=Runtime  {R}3{END}=Logic : ").strip()
        if ans in BUG_TYPES:
            return BUG_TYPES[ans]
        print("  Choose 1, 2 or 3.")


def reveal(ch):
    print(f"\n  {BOLD}Answer:{END} line {' or '.join(map(str, ch['bug']))}  "
          f"| {ch['type']} error")
    print(f"  {C}Why:{END}  {ch['explain']}")
    print(f"  {G}Fix:{END}  {ch['fix']}\n")


def scoreboard(teams, scores, final=False):
    title = "FINAL SCORES" if final else "Scoreboard"
    print(f"  {BOLD}{title}{END}")
    for name in sorted(teams, key=lambda t: -scores[t]):
        print(f"   {name:<15} {Y}{scores[name]:>4}{END} pts")
    print()


# ---------- main game ----------
def play():
    clear()
    banner()
    n = input("  How many teams (1-4)? ").strip()
    n = int(n) if n.isdigit() and 1 <= int(n) <= 4 else 2
    teams = []
    for i in range(n):
        name = input(f"  Name of team {i + 1}: ").strip() or f"Team {i + 1}"
        teams.append(name)

    total = len(CHALLENGES)
    r = input(f"  How many rounds (1-{total}, Enter = {min(12, total)})? ").strip()
    rounds = int(r) if r.isdigit() and 1 <= int(r) <= total else min(12, total)

    # pick a balanced set, then order Easy -> Medium -> Hard
    order = {"Easy": 0, "Medium": 1, "Hard": 2}
    picked = random.sample(CHALLENGES, rounds)
    picked.sort(key=lambda c: order[c["level"]])

    scores = {t: 0 for t in teams}
    streak = {t: 0 for t in teams}

    for rnd, ch in enumerate(picked, 1):
        team = teams[(rnd - 1) % len(teams)]
        clear()
        print(f"  {BOLD}Round {rnd}/{rounds}{END}   Turn: {M}{BOLD}{team}{END}\n")
        show_code(ch)

        start = time.time()
        line, hinted = ask_line(ch, f"  {team}, which line has the bug? (h = hint): ")
        elapsed = time.time() - start
        points = -3 if hinted else 0

        if line in ch["bug"]:
            points += 10
            msg = f"  {G}Correct line! +10{END}"
            if elapsed <= 30:
                points += 3
                msg += f"  {C}Speed bonus +3 ({elapsed:.0f}s){END}"
            print(msg)
            if ask_type() == ch["type"]:
                points += 5
                print(f"  {G}Right bug type! +5{END}")
            else:
                print(f"  {R}Wrong bug type.{END}")
            streak[team] += 1
            if streak[team] == 3:
                points += 5
                streak[team] = 0
                print(f"  {Y}{BOLD}3 in a row! Streak bonus +5{END}")
        else:
            print(f"  {R}Not that line.{END}")
            streak[team] = 0
            # steal chance for the next team
            if len(teams) > 1:
                stealer = teams[rnd % len(teams)]
                s, _ = ask_line(ch, f"  {stealer}, STEAL! Which line? ")
                if s in ch["bug"]:
                    scores[stealer] += 5
                    print(f"  {G}Stolen! {stealer} +5{END}")
                else:
                    print(f"  {R}Missed the steal.{END}")

        scores[team] += points
        reveal(ch)
        scoreboard(teams, scores)
        input("  Press Enter for the next round...")

    clear()
    banner()
    scoreboard(teams, scores, final=True)
    best = max(scores.values())
    winners = [t for t in teams if scores[t] == best]
    print(f"  {G}{BOLD}Winner: {' & '.join(winners)}!{END}  Great debugging!\n")


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        print(f"\n  {Y}Game ended. Bye!{END}")
