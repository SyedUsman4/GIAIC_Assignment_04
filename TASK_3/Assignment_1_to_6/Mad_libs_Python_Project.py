def generate_story_logic(noun, adjective, verb):
    return f"One fine morning, a {adjective} {noun} decided to {verb} through the bustling city, marveling at the sights and sounds."

def main():
    print("📝 Mad Libs Story Generator")
    print("===========================")
    
    # Input fields
    noun = input("Enter a noun (e.g., cat): ").strip()
    adjective = input("Enter an adjective (e.g., fluffy): ").strip()
    verb = input("Enter a verb (e.g., jumps): ").strip()
    
    # Validate input
    if not noun or not adjective or not verb:
        print("🚨 Please enter all required words!")
        return
    
    if any(" " in word or "," in word for word in [noun, adjective, verb]):
        print("🚨 Please enter only one word per field without spaces or commas!")
        return
    
    # Generate and display the story
    story = generate_story_logic(noun, adjective, verb)
    print("\n🎉 Your Generated Story:")
    print("-----------------------")
    print(story)

if __name__ == "__main__":
    main()