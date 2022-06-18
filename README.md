# Mr Hangman 

# Aim of this project

Mr Hangman is a Python terminal game, that runs on the Code Institue mock terminal called Heroku.The site is aimed at users who would like to enjoy a game of Hangman. The game generates a random word to which the player has 6 attempts per word before the game is over.


# User Goals 

* The game should be easy to play
* The program to be relatively simple to nagivate
* The game to be fun and challenging for user
* The game to have little to no bugs
* Approriate response to player/user inputs

# **Features** #

* Home page/Main menu
  * View game header
  * Option to select start game
  * Option to select game rules
  * Option to exit the game

  ![Main screen](/screenshots/Main%20menu.png) 

* Game Rules
  * Simple and short display of the game rules followed by a function that requires user to press enter 
  in order to back to the menu

  ![Game Rules](/screenshots/Game%20Rules.png)

* Game Play
  * After selecting Option 1 to start game, the user is then prompted to input their name. After the user inputs their
  name, a good luck message pops up before the game begins. A random word is generated and the game starts with the hidden word showing how many letters are in it"

  ![Start of game](/screenshots/Game%20play.png)

* Correct guess
  * Once the game has started, the player is then presented with the hidden word to be guessed. The player can also see
  how many letter are in the hidden word. If a letter is guessed correctly, the empty space is then replaced by the correct letter. If a letter guessed features more than once on the hidden word, the empty space will be replaced by the correct letter accordingly.


  ![Correct guess](/screenshots/Correct%20guess.png)


* Incorrect guess 
  * If the letter guessed by the user is not in the hidden word, the amount of attempts the user has reduces by 1 
  and thus, adds a body part to the gallows. A message appears informing the user that the letter guessed is not in the hidden word. The incorrect letter is also added to the list of guessed letters.


  ![Incorrect guess](/screenshots/Incorrect%20guess.png)


* Invalid guess
  * When the user/player inputs anything other than a letter (i.e digits, special characters, or multiple letters). this will prompt an error message to show up on the program, where the user will be encouraged to make another guess.
  This will not affect the amount of attempts the user has.


  ![Invalid guess](/screenshots/Invalid%20guess.png)

* Winner 
  * The player is the winner when the player guesses all the letters in the hidden word. The player is then presented with the option of playing the game again or not


  ![Player wins](/screenshots/Player%20wins.png)


* Game Over 
  * If the player has 6 incorrect guesses, the player is hung. The hidden word is then revealed and the player is presented with the option of playing the game again or not. If the player chooses to play again, the game will start over again. If the option selected is to not play again, the player is then prompted to head back to the main menu


  ![Game over](/screenshots/Game%20over.png)

* Invalid inputs
  * Checks are ran to ensure that no invalid inputs are submitted to the program
  * For every invalid inputs, an error message is displayed on the program and the user is then asked to input their selections again


  ![Invalid input](/screenshots/Invalid%20input%201.png)
  ![Invalid input](/screenshots/invalid%20input%202.png)
  ![Invalid input](/screenshots/Invalid%20input%203.png)
  ![Invalid input](/screenshots/Invalid%20input%204.png)
  ![Invalid input](/screenshots/Invalid%20input%205.png)
  ![Invalid input](/screenshots/Invalid%20input%206.png)

# Future features to implement 

* Add scoring system, with the 10 best scores to be shown on the leaderboard
* 1 feature to implement in the future are difficulty levels. This could be for example making an easy level consist of words with less than 4 letters. Intermediate level consisting of 5-7 letters and a hard level with 8 letters and above in a word. This will give the user the ability to test him/herself
* A timer could be added to the game, where a different timer could be set according to difficulty level(shorter timer for easy level)
* Add colors, this would make the program more interactive and interesting for the user.
* Divide the words into categories(i.e sports, science, geography, animals, verbs etc...)




