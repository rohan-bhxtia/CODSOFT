import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_-+=<>?"

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Check if the password length is valid
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired password length: "))

    # Generate and display the password
    password = generate_password(length)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
