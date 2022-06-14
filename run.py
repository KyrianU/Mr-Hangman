import random
import string 
from words import words 


def get_random_word(words):
    """
    Generates a random word from the words.py
    """
    word = random.choice(words)
    while "-" in word or " " in words:
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

def menu():
    """
    Displays menu choices
    """
    menu_choices = True
    while menu_choices:
        print('Press 1 to start the game')
        print('press 2 to for the rules of the game')
        print('press 3 to exit the game')
        choice = input('Choose one of the menu options')
        if choice == '1':
            menu_choices = False
            player_name()
            start_game()
        elif choice == '2':
            menu_choices = False
        elif choice == '3':
            menu_choices = False
            print('Thanks for playing, see you soon!')
        else:
            print(f'sorry, {choice} is not a valid option, please choose 1,2 or 3')
            menu()



        


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
            menu()
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
    hidden_word = " _ " * len(word)
    letters_in_word = set(word)
    letters_guessed = set()
    attempts = 6
    print(hidden_word)
    alpha = set(string.ascii_uppercase)
    print("All the best!")
    print(f'attempts left: {attempts}')
    

    while len(letters_in_word) and attempts > 0:
        print(" Letters Guessed: ", " ".join(letters_guessed))
        print(f'attempts remaining: {attempts}')
        guess = input('Please pick a letter: \n').upper()

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
        print(f'You have lost. the hidden word was {word}')
        start_game()
    else:
        print('congrats')
        start_game()


    
   
    
        
                
        
    

  

if __name__ == "__main__":
    """
    Start game
    """
    menu()



    
        
