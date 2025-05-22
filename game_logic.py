import snowman
import ascii_art
import random

def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def get_user_guess():
    char_alphabet = "abcdefghijklmnopqrstuvwxyz" #Only lowercase because on input we convert to lower()
    while True:
        try:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess in char_alphabet:
                return guess
            else:
                print("Ensure that is only a single alphabetical character")
        except ValueError:
            print("Please enter a character")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(ascii_art.STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman! ☃️")
            break

        # Loss condition
        if mistakes >= max_mistakes:
            print(ascii_art.STAGES[mistakes])
            print(f"Game over! The snowman melted. The word was: {secret_word}")
            break

        # Prompt user for a guess
        guess = get_user_guess()

        # Skip if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        # Add guess to guessed_letters
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            print("Incorrect guess.\n")
            mistakes += 1
