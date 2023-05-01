def encrypt(message, shift):
    """Encrypts the given message using Caesar cipher."""
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result.upper()

def decrypt(message, shift):
    """Decrypts the given message using Caesar cipher."""
    return encrypt(message, -shift)

def get_valid_mode():
    """Prompts the user to enter a valid mode (encrypt or decrypt)."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode == "e" or mode == "d":
            return mode
        else:
            print("Invalid mode. Please enter either 'e' or 'd'.")

def get_valid_message():
    """Prompts the user to enter a message to encrypt or decrypt."""
    return input("What message would you like to encrypt or decrypt? ")

def get_valid_shift():
    """Prompts the user to enter a valid shift value."""
    while True:
        try:
            shift = int(input("What is the shift number? "))
            return shift
        except ValueError:
            print("Invalid shift value. Please enter an integer.")

def run_program():
    """Runs the Caesar cipher program."""
    print("Welcome to the Caesar Cipher")
    while True:
        mode = get_valid_mode()
        message = get_valid_message()
        shift = get_valid_shift()
        if mode == "e":
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        while True:
            choice = input("Would you like to encrypt or decrypt another message? (y/n) ").lower()
            if choice == "y":
                break
            elif choice == "n":
                print("Thanks for using the program, goodbye!")
                return
            else:
                print("Invalid input. Please enter either 'y' or 'n'.")

if __name__ == "__main__":
    run_program()
print("\033[91m{}\033[0m".format("This text is in red."))
