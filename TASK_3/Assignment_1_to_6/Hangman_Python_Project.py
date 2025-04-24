import random

def choose_word():
    """Select a random word from a predefined list."""
    words = ["python", "hangman", "programming", "developer", "algorithm", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters filled in and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_user_guess(guessed_letters):
    """Get a valid letter guess from the user."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("🚨 Please enter a single letter!")
        elif not guess.isalpha():
            print("🚨 Please enter a valid letter!")
        elif guess in guessed_letters:
            print("🚨 You already guessed that letter!")
        else:
            return guess

def main():
    print("🎮 Hangman Game")
    print("===============")
    print("Guess the word one letter at a time. You have 6 lives!")
    
    # Initialize game state
    word = choose_word()
    guessed_letters = set()
    lives = 6
    
    while lives > 0:
        # Display current state of the word
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Lives left: {lives}")
        
        # Get user's guess
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess not in word:
            lives -= 1
            print(f"❌ The letter '{guess}' is not in the word.")
        else:
            print(f"✅ The letter '{guess}' is in the word!")
        
        # Check if the user has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    
    # If the user runs out of lives
    if lives == 0:
        print("\n💀 Game over! You ran out of lives.")
        print("The word was:", word)

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing! Goodbye! 🎮")

if __name__ == "__main__":
    main()