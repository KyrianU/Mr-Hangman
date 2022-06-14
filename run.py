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


def play_game():
    """
    Starts the game for user, a random word is then generated from the
    words.py file for user to guess. Player will then guess how many letters are 
    in the word
    """
    word = get_random_word(words).upper()
    hidden_word = '_' * len(word)
    letters_in_word = set(word)
    letters_guessed = set()
    attempts = 6
    alpha = set(string.ascii_uppercase)
    print("All the best!")
    print(f'attempts left: {attempts}')
    print(f'the hidden word is {hidden_word}')

    while len(letters_in_word) and attempts > 0:
        print(" Letters Guessed: ", " ".join(letters_guessed))
        print(f'attempts remaining: {attempts}')
        guess = input('Please pick a letter: ').upper()

        if guess in alpha - letters_guessed:
            letters_guessed.add(guess)
            if guess in letters_in_word:
                letters_in_word.remove(guess)
                print('')
            else:
                attempts -= 1
                print(f'{guess} is not in the hidden word')
        elif guess in letters_guessed:
            print(f'You have already tried {guess}')
        else:
            print('Invalid character, please choose letters only')

    if attempts == 0:
        print(f'oops you dead. the hidden word was {hidden_word}')
        start_game()
    else:
        print('congrats')
        start_game()


    
   
    
        
                
        
    

  

if __name__ == "__main__":
    """
    Start game
    """
    player_name()



    
        
