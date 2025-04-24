def main():
    AFFIRMATION = "I am capable of doing anything I put my mind to."
    
    print("Please type the following affirmation: ")
    print(AFFIRMATION)

    user_feedback = input("> ")  # Get user's input
    
    while user_feedback != AFFIRMATION:  # Repeat until the correct affirmation is entered
        print("\nThat was not the affirmation. Try again!")
        print("Please type the following affirmation: ")
        print(AFFIRMATION)
        user_feedback = input("> ")

    print("\nThat's right! 😊")

# Required to run the main function
if __name__ == "__main__":
    main()