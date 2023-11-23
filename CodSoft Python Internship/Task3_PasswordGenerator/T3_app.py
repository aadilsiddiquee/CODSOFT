import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine selected character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        print("Error: At least one character set should be selected.")
        return None

    # Generate a random password using the specified length
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("\n == Welcome to the Password Generator! == \n")

    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("\n Enter the desired length of the password: "))

        # Ask for user preferences
        use_lowercase = input("\n Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_uppercase = input("\n Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("\n Include numbers? (yes/no): ").lower() == 'yes'
        use_special_chars = input("\n Include special characters? (yes/no): ").lower() == 'yes'
    except ValueError:
        print("\n Invalid input. Please enter a valid number.")
        return

    # Generate the password
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

    # Display the generated password
    if password:
        print("\n Generated Password:", password, "\n")

if __name__ == "__main__":
    main()
