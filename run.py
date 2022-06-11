import random
from words import words 


print(
    """
    Welcome to Mr HangMan game!
    The rules are pretty simple, you are given a random word,
    to which you have 6 attempts at guessing before Mr HangMan is hung
    Best of luck!
    """
)

def get_random_word (words):
    """
    Generates a random word from the words.py
    """
    word = random.choice(words)
    while '-' in word " " in words:
        word = random.choice(words)
    return word.upper()