
import string


def check_password_strength(password):
    # Check password requirements
    length_ok = len(password) >= 8

    uppercase_ok = any(
        ch.isupper() for ch in password
    )

    number_ok = any(
        ch.isdigit() for ch in password
    )

    symbol_ok = any(
        ch in string.punctuation for ch in password
    )

    # Calculate score
    score = sum([
        length_ok,
        uppercase_ok,
        number_ok,
        symbol_ok
    ])

    # Decide password strength
    if score <= 1:
        strength = "WEAK"
    elif score <= 3:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    # Display results
    print("\n--- CHECK RESULTS ---")

    print("Length at least 8 characters:",
          "PASS" if length_ok else "FAIL")

    print("Contains uppercase letter:",
          "PASS" if uppercase_ok else "FAIL")

    print("Contains a number:",
          "PASS" if number_ok else "FAIL")

    print("Contains a symbol:",
          "PASS" if symbol_ok else "FAIL")

    print("\nPassword strength:", strength)


def main():
    print("=" * 40)
    print("    PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter a sample password: ")

    if password == "":
        print("Please enter a password.")
    else:
        check_password_strength(password)


if __name__ == "__main__":
    main()
