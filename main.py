import random


def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer", "debugging", "syntax", "variable"]

    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print("Welcome to Hangman!")

    secret_word = choose_word()

    guessed_letters = []

    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        # Display the current state of the word
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue


        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in secret_word:
            attempts += 1
            print(f"Incorrect! Attempts left: {max_attempts - attempts}")


        if set(secret_word) == set(guessed_letters):
            print("Congratulations! You guessed the word!")
            break


    if attempts == max_attempts:
        print(f"\nSorry, you ran out of attempts. The word was '{secret_word}'.")


if __name__ == "__main__":
    hangman()
