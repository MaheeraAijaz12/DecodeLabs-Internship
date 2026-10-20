# Password Strength Checker

## Project Overview
This project is a simple Python program that checks password strength based on four requirements:

- At least 8 characters long
- Contains an uppercase letter
- Contains a number
- Contains a symbol (such as `!`, `@`, or `#`)

The program displays whether each requirement passes or fails and gives an overall result: **WEAK**, **MEDIUM**, or **STRONG**.

## Requirements
- Python 3
- No extra packages are needed; the program uses Python's built-in `string` module.

## How to Run
1. Download or clone this repository.
2. Open a terminal or run the file in an IDE such as Spyder.
3. Run `password_strength_checker.py`.
4. When prompted, enter a sample password to test.

```bash
python password_strength_checker.py
```

## How Strength Is Calculated
The program checks four conditions: length of at least 8 characters, uppercase letter, number, and symbol. Each condition that passes adds one point.

- **WEAK:** 0–1 points
- **MEDIUM:** 2–3 points
- **STRONG:** 4 points

## Main File
- `password_strength_checker.py` — source code for the Password Strength Checker.

## Note
For privacy, use a sample password for testing rather than entering a password you actually use.
