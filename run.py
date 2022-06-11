import random
from words import words 
import string 


print(
    """
    Welcome to Mr HangMan game!
    The rules are pretty simple, you are given a random word,
    to which you have 6 attempts at guessing before Mr HangMan is hung
    Best of luck!
    """
)

def get_random_word(words):
    """
    Generates a random word from the words.py
    """
    word = random.choice(words)
    while '-' in word or " " in words:
        word = random.choice(words)
    return word.upper()


def player_name():
    """
    Requires user to input their names
    """

    while True: 
        name = input('Please enter your name: ')
        if name.isalpha():
            print(f'Welcome to the game {name}, best of luck')
            start_game()
            break
        else:
            print('Invalid name, please use letters only')


def start_game():
    """
    function that gives the player the choice to start the game.
    Also give the option for the player to play again once the round has ended
    """
    while True:
        print('would you like to start the game?')
        start_game = input("Press 'Y for Yes and press 'N for No\n")

        if start_game == 'Y':
            play_game()
            break 
        elif start_game == 'N':
            end_game()
            break
        else:
            print("Invalid input, please choose between 'Y' or 'N' ")

  

    
        
