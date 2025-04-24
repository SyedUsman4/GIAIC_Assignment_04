import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    print("=====================")
    
    # Get the number of passwords to generate
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            print("🚨 Please enter a positive number!")
            return
    except ValueError:
        print("🚨 Invalid input! Please enter a number.")
        return
    
    # Get the length of each password
    try:
        password_length = int(input("Enter the length of each password: "))
        if password_length <= 0:
            print("🚨 Please enter a positive number!")
            return
    except ValueError:
        print("🚨 Invalid input! Please enter a number.")
        return
    
    # Generate and display the passwords
    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(password_length)
        print(f"Password {i + 1}: {password}")
    
    # Ask if the user wants to generate more passwords
    play_again = input("\nDo you want to generate more passwords? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for using the Password Generator! Goodbye! 🔐")

if __name__ == "__main__":
    main()