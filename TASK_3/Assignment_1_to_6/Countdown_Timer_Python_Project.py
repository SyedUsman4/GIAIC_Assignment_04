import time

def countdown_timer(seconds):
    """Run a countdown timer for the specified number of seconds."""
    while seconds:
        # Calculate minutes and seconds
        mins, secs = divmod(seconds, 60)
        # Format the time as MM:SS
        timer = f"{mins:02d}:{secs:02d}"
        # Print the timer
        print(timer, end="\r")  # Use \r to overwrite the previous line
        # Wait for 1 second
        time.sleep(1)
        # Decrease the remaining time
        seconds -= 1
    
    # Print a message when the timer ends
    print("⏰ Time's up!")

def main():
    print("⏳ Countdown Timer")
    print("==================")
    
    # Get the countdown duration from the user
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        if seconds <= 0:
            print("🚨 Please enter a positive number of seconds!")
            return
    except ValueError:
        print("🚨 Invalid input! Please enter a number.")
        return
    
    # Start the countdown
    print("\nStarting countdown...")
    countdown_timer(seconds)

    # Ask if the user wants to start another timer
    play_again = input("\nDo you want to start another timer? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for using the Countdown Timer! Goodbye! ⏳")

if __name__ == "__main__":
    main()