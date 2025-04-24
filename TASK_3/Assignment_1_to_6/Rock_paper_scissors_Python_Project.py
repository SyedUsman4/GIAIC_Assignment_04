import random

def get_user_choice():
    """Get the user's choice (rock, paper, or scissors)."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("🚨 Invalid chorockice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Get the computer's random choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("🎮 Rock, Paper, Scissors Game")
    print("=============================")
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye! 🎮")
            break

if __name__ == "__main__":
    main()