import random
import string
from words import words
from gallows import hangman_stages


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
    Requires user to input their names.
    """

    while True:
        name = input('Please enter your name: \n')
        if name.isalpha():
            print(f'Welcome to the game {name}, best of luck! \n')
            play_game()
            break
        else:
            print('Invalid name, please use letters only')


def enter():
    """
    function specifically written for option 2
    of the menu function and 'N' option in the game_end
    function. This function enablesplayer to press Enter
    and will take them back to the main menu
    """
    input('Press Enter to go back to the Menu')


def game_rules():
    """
    Displays the rules of the game
    """
    print(
       """
       Welcome to Hangman!
       The rules are very simple, you are given a random word,
       each unsuccessful attempts at guessing a letter adds a new body
       part to the gallows. After 6 uncessful attempts the player will be
       hunged and the game is over. To win the game, the player has to guess
       the full word within the allocated 6 attempts.

       Best of luck!
       """)
    print('\n')
    enter()
    menu()


def menu():
    """
    Displays menu choices
    """
    menu_choices = True
    while menu_choices:
        print('Press 1 to start the game')
        print('press 2 to for the rules of the game')
        print('press 3 to exit the game \n')
        choice = input('Choose one of the menu options: \n')
        if choice == '1':
            menu_choices = False
            player_name()
            play_game()
        elif choice == '2':
            menu_choices = False
            game_rules()
        elif choice == '3':
            menu_choices = False
            print('Thanks for playing, see you soon...')
            exit()
        else:
            print(f'sorry,{choice} is not valid, please choose 1,2 or 3')
            menu()


def game_end():
    """
    End of the game option, user will have the option
    to play again or the quit the game and be directed
    back to the main menu"
    """
    while True:
        print('Would you like to play again?')
        play_again = input("Press 'Y for Yes or 'N' for No \n")

        if play_again == 'Y':
            play_game()
            break
        elif play_again == 'N':
            print('Thanks for playing. See you soon...\n')
            enter()
            menu()
        else:
            print("Invalid input, please chose between 'Y' or 'N \n")


def play_game():
    """
    Starts the game for user, a random word
    is then generated from thewords.py file
    for user to guess. Player will then guess
    how many letters are in the word
    """
    word = get_random_word(words).upper()
    hidden_word = "_" * len(word)
    letters_in_word = set(word)
    letters_guessed = set()
    attempts = 6
    print(hidden_word)
    alpha = set(string.ascii_uppercase)
    print(f'attempts left: {attempts}')

    while len(letters_in_word) and attempts > 0:
        word_completion = [letter if letter in letters_guessed
                           else '_' for letter in word]
        print("Letters guessed: ", " ".join(letters_guessed))
        print(f'Attempts remaining: {attempts}')
        print('Hidden word: ', ''.join(word_completion))
        print(hangman_stages(attempts))
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
        print(hangman_stages(attempts))
        print(f'You have been hanged. The hidden word was {word}')
        game_end()
    else:
        print('congrats')
        game_end()


if __name__ == "__main__":
    """
    Start game
    """
    menu()
