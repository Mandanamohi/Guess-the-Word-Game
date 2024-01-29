def check_guess(guessed_letter, word):
   
    # Step 2: Convert the guess into lowercase
    guessed_letter = guessed_letter.lower()

    # Step 3: Check if the guess is in the word
    return guessed_letter in word.lower()

def check_guess(guessed_letter, word):
    """
    Check if the guessed letter is in the word.

    Parameters:
    - guessed_letter (str): The guessed letter.
    - word (str): The word to guess.

    Returns:
    - bool: True if the guessed letter is in the word, False otherwise.
    """
    # Step 2: Convert the guess into lowercase
    guessed_letter = guessed_letter.lower()

    # Step 3: Check if the guess is in the word
    return guessed_letter in word.lower()

def ask_for_input(word):
   
    while True:
        # Iteratively check if the input is a valid guess
        user_input = input("Enter your guess (a single letter): ")

        if len(user_input) == 1 and user_input.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            result = check_guess(user_input, word)
            if result:
                print(f"Congratulations! '{user_input}' is in the word.")
            else:
                print(f"Sorry, '{user_input}' is not in the word.")
            return result  # Return the result to indicate if the guess is in the word
        else:
            print("Please enter a valid single letter.")

# Step 4: Test the code
secret_word = "Python"
ask_for_input(secret_word)