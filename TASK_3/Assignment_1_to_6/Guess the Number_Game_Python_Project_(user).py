import random

def main():
    print("🎮 Guess the Number Game")
    print("========================")
    print("Try to guess the secret number between 1 and 10!")
    
    # Initialize game state
    secret_number = random.randint(1, 10)
    attempts = 0
    hints = []
    
    while True:
        # Get user's guess
        try:
            guess = int(input("Enter your guess (1-10): "))
            if guess < 1 or guess > 10:
                print("🚨 Please enter a number between 1 and 10!")
                continue
        except ValueError:
            print("🚨 Invalid input! Please enter a number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number **{secret_number}** in {attempts} attempts!")
            break
        else:
            # Provide a hint
            if guess < secret_number:
                hint = "The secret number is higher."
            else:
                hint = "The secret number is lower."
            hints.append(f"💡 Hint: {hint}")
            print(hint)
    
    # Show all hints at the end
    print("\n💡 All Hints:")
    for hint in hints:
        print(hint)
    
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing! Goodbye! 🎮")

if __name__ == "__main__":
    main()