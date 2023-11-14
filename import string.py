import string
import random

def generate_password(length):
    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the minimum length for a strong password
    if length < 6:
        print("Password length should be at least 66 characters.")
        return None

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Use random.sample to ensure each character category is represented
    password = random.sample(lowercase_letters, 1) + random.sample(uppercase_letters, 1) + \
               random.sample(digits, 1) + random.sample(special_characters, 1) + \
               random.sample(all_characters, length - 4)

    # Shuffle the password to make the order random
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

def main():
    try:
        # Get the desired password length from the user
        password_length = int(input("Enter the desired password length: "))
        
        # Generate the password
        password = generate_password(password_length)

        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
