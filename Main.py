" Enter Your Code Here" 
"""Define a dictionaries of guesses you would want to use"""

"""Feel free to use any method to have your words defined, plus a theme, be it from a file. 
    Here is an example of a key and value combination reflecting the words within the topic."""

import random

# Define themes and words
Themes = {
    "History": [
        "marco polo",
        "napoleon",
        "mesopotamia",
        "persia",
        "world war"
    ],
    "Computers": [
        "bus",
        "semiconductor",
        "keyboard",
        "vacuum tube",
        "nanometer"
    ],
    "Cars": [
        "dodge",
        "toyota",
        "daihatsu",
        "displacement",
        "stroke"
    ]
}

def hangman():
    # Select a random theme and word
    names = list(Themes.keys())
    chosen_theme = random.choice(names)
    word_choice = random.choice(Themes[chosen_theme])

    
    print("Welcome to Hangman!")
    print(f"\nTheme: {chosen_theme.capitalize()}")
    # print('Enter the word "hint" if you need help (you lose 1 attempt).')

    # Initialize game variables
    attempts = 18
    guessed_letters = set() # save letters used
    revealed_word = ''.join(['_' if char != ' ' else ' ' for char in word_choice]) # hides word_choice with dashes

    while attempts > 0:
        print(f"\nWord: {revealed_word}") # displays dashes 
        print(f"Attempts remaining: {attempts}") # display remaining attempts
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}") # replace guessed letters with the dashes

        user_input = input("Enter a letter or 'hint': ") 

        # if user_input == "hint":
        #     attempts -= 1
        #     print(f"Hint: The word relates to {chosen_theme}.")
        #     continue

        # rejects multiple inputs
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # prevet guessed letter from being input more than once
        if user_input in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(user_input) # adds guessed letter to list

        # reveals guessed letters position and replaces the dash with the letter
        if user_input in word_choice:
            print("Good guess!")
            revealed_word = ''.join(
                [char if char in guessed_letters or char == ' ' else '_' for char in word_choice]
            )
        else: # reduce number of guesses
            print("Wrong guess.")
            attempts -= 1

        # Check wining condition. that all dashes are all replaced.
        if '_' not in revealed_word:
            print(f"\nCongratulations! You guessed the word: {word_choice}")
            break
    else: # if attemps reach 0
        print(f"\nYou ran out of attempts. The word was: {word_choice}. Better luck next time!")

# Run the game
if __name__ == "__main__": # checks whether the script is run directly or being imported
    hangman()
