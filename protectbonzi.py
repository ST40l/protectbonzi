import random
import string
import pyttsx3

def bonzi_buddy_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "As an artificial intelligence, I don't have emotions, but I'm here to help you!",
        "what's your name": "My name is similar to BonziBuddy, and I'm a Python application.",
        "thank you": "You're welcome! I'm glad I could help.",
        "goodbye": "Goodbye, have a great day!"
    }

    response = responses.get(user_input.lower(), "I'm sorry, I didn't understand. Could you please repeat?")
    return response

def is_valid_input(user_input):
    # Ensure user input is not empty
    if not user_input.strip():
        return False

    # Clean user input and only allow alphanumeric characters
    cleaned_input = ''.join(filter(str.isalnum, user_input))

    # Compare the cleaned input with the original input
    if cleaned_input.lower() != user_input.lower():
        return False

    return True

def print_bonzibuddy():
    bonzibuddy = """
    -------------------------
      \                   /    
        \    O     O    /
          \     ^     /
            \_______/     
            /               \  
          /    |     |     |    \ 
         /     |     |     |     \ 
       /       |     |     |       \ 
     /         |     |     |         \ 
    -------------------------
    """
    print(bonzibuddy)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("Hello! I am a Python application similar to BonziBuddy. How can I assist you?")
    
    while True:
        user_input = input("> ")

        # Exit the program if the user wants to quit
        if user_input.lower() == "exit":
            print("Goodbye, have a great day!")
            break

        # Check if the user's input contains the phrase "protect me" and warn them about DDoS attacks
        if "protect me" in user_input.lower():
            print("WARNING: This application cannot provide full protection against DDoS attacks. Please use caution.")
            continue

        # Validate user input
        if not is_valid_input(user_input):
            print("Please enter a valid input.")
            continue

        response = bonzi_buddy_response(user_input)
        print_bonzibuddy()
        print(response)

        # Speak the response out loud
        speak(response)

if __name__ == "__main__":
    main()
