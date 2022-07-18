# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user input
    while len(word_letters) > 0:

        # letter used
        print("You have used these letters: ", " ".join(used_letters))

        # what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(word_list)

        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that letter. Please guess again")
        else:
            print("Invalid character")

        print(word_letters)


if __name__ == '__main__':
    hangman()
