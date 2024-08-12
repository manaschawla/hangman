# hangman-game 
OVERVIEW
Welcome to the Hangman Game!This is a simple game where the player have to guess the word by entring one
 letter at a time.
 the player has limited number of chances and chances reduces with each incorrect guess.

 FEATURES
 1. Randomly selects words from a predefined list.
 2. Interactive gameplay with user inputs.
 3. It tracks the chances of the user and display chances with each input.
 4. It displays current state of word with correct guesses filled and the unknown words as guesses.
 5. Provides a victory message when word is guessed correctly and a lose message if the player lost the game.

 HOW THE GAME WORKS
 1. Objective:
 -The objective is to guess the hidden word by guessing the letter within a limited number of chances.

 2. Gameplay:
 -The game starts by randomly selecting a word from the predefined list.
 -The selected word is repersented with dashes(eg _ _ _ _ _ for a five letter word).
 -You have 5 chances to guess the word.

 3. Guessing a letter:
 -Each turn, you input a single letter as your guess.
 -If the letter is present in the word,it will replace the corresponding dash.
 -If the letter is not in the word,you  lose one chance.

 4. Winning and Losing:
 -You win the game if you guess all the letters in the word before running out of chances.
 -You lose the game if you run out of chances before guessing the word.

 REQUIREMENTS:
 1. Python: 
 -Ensure you have Python 3.x installed on your machine.
 -No additional libraries or dependencies are needed.

 HOW TO RUN THE GAME:
 1. Copy the code into a file named hangman.py.
 2. Open a terminal or command prompt.
 3. Navigate to the directory where hangman.py is located.
 4. Run the game using the command:
 5. Follow the instructions displayed on the screen to start guessing the word.
 
 ABOUT THE CODE:
 1. Word Selection:
 A word is randomly chosen from the WORDS list.
 2. User Input:
  The player inputs a single letter to guess.
 3. Feedback:
  The game provides feedback using logging messages (INFO for game progress, DEBUG for internal details, WARNING for incorrect guesses).
 4. Chances:
  The player has 5 chances to guess the word before losing the game.
 5. End Game:
  The game ends when the player either successfully guesses the word or runs out of chances.

 TIPS FOR PLAYING:
 1. Start by guessing common vowels like 'a', 'e', 'i', 'o', 'u'.
 2. Pay attention to the position of correct guesses to help figure out the remaining letters.
 3. Remember, you only have 5 chances, so guess wisely! 




