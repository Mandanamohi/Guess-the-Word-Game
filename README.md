def check_guess(guessed_letter, word):
    guessed_letter = guessed_letter.lower()
    return guessed_letter in word.lower()

def ask_for_input(word):
    while True:
        user_input = input("Enter your guess (a single letter): ")

        if len(user_input) == 1 and user_input.isalpha():
            result = check_guess(user_input, word)
            if result:
                print(f"Congratulations! '{user_input}' is in the word.")
            else:
                print(f"Sorry, '{user_input}' is not in the word.")
            return result
        else:
            print("Please enter a valid single letter.")

# Example usage:
secret_word = "Python"
ask_for_input(secret_word)
