
# Cyber Security Project 2
# Basic Encryption and Decryption
# Technique: Caesar Cipher


def encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        # Encrypt uppercase letters
        if 'A' <= char <= 'Z':
            new_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )
            encrypted_text += new_char

        # Encrypt lowercase letters
        elif 'a' <= char <= 'z':
            new_char = chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a')
            )
            encrypted_text += new_char

        # Keep spaces, numbers and symbols unchanged
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    # Reverse the encryption shift
    return encrypt(text, -shift)


def main():
    print("=" * 40)
    print(" CYBER SECURITY PROJECT 2")
    print(" Basic Encryption & Decryption")
    print(" Technique: Caesar Cipher")
    print("=" * 40)

    # Take input from the user
    message = input("\nEnter your message: ")

    # Validate message
    if not message.strip():
        print("Error: Message cannot be empty.")
        return

    # Take and validate shift key
    try:
        shift = int(input("Enter shift key (0-25): "))
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if not 0 <= shift <= 25:
        print("Error: Shift key must be between 0 and 25.")
        return

    # Perform encryption
    encrypted_text = encrypt(message, shift)

    # Perform decryption
    decrypted_text = decrypt(encrypted_text, shift)

    # Display results
    print("\n" + "=" * 40)
    print("           RESULTS")
    print("=" * 40)

    print("Original Text:   ", message)
    print("Encrypted Text:  ", encrypted_text)
    print("Decrypted Text:  ", decrypted_text)

    # Verify the result
    if message == decrypted_text:
        print("\nStatus: Encryption and decryption successful!")
    else:
        print("\nStatus: Verification failed!")

    print("=" * 40)


# Start the program
if __name__ == "__main__":
    main()
