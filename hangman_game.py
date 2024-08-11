"""this code is for hangman game in which you have to guess the word"""


import random
import logging
#pylint:disable =W1203
#setting up logging to show debug and info messages.
logging.basicConfig(level=logging.INFO)
#list of words that user have to guess.
WORDS = ["grace", "trust", "honor", "faith", "truth", "peace", "unity", "hope", "love",
         "care", "kind", "brave", "strong", "wise", "calm", "clear", "pure", "just", "fair", 
         "noble", "humble", "bright", "smart", "happy", "proud", "loyal", "honest", "joyful",
         "patient", "gentle", "bold", "calm", "vivid", "alert", "sharp", "keen", "quick", 
         "solid", "firm", "true", "grand", "good", "great", "worthy", "steady", "sound", "brisk",
         "swift", "free", "fresh", "kind", "mild", "rich", "wise", "calm", "deep", "calm", "calm",
         "sweet", "pure", "bright", "calm", "dear", "soft", "mild", "warm", "cool", "calm", "light",
         "high", "long", "wide", "deep", "full", "calm", "calm", "pure", "clean", "fine", "fair",
         "glad", "neat", "bright", "kind", "safe", "good", "pure", "fine", "fair", "neat", "calm",]
#Initialize the chances.
CHANCES = 5
#Welcome The User And tell him the rules and given chances.
logging.info(f"""WELCOME TO THE HANGMAN GAME.
             You Have To Guess the word correctly.
             you have {CHANCES} chances to guess the word correctly.""")
#make the os ramdomly choose a word
chosen_word = random.choice(WORDS)
#check the word is choosen correcty.
logging.debug(f"the chosen word is : {chosen_word}")
#Get the leength of the choosen word.
word_length = len(chosen_word)
logging.debug(word_length)
#initialize the dashes variable with '_' and multiply mariable
dashes = '_' *  word_length
logging.info(dashes)
#Start an Infinite Loop,until a user wins or lose.
while True:
    print(f"you have chances left: {CHANCES}")
    #Take input from the user.
    guess = input("enter your guess: ")
    #check if guessed letter is in choosen word.
    if guess in chosen_word:
        logging.info("you have guessed correct.")
        #Initialize an empty string.
        new_string = ""
        #make use of enumerate here.
        for index, charecter in enumerate(dashes):
            if guess == chosen_word[index]:
                new_string += chosen_word[index]
            else:
                new_string += dashes[index]
        dashes =  new_string
        print(dashes)
        #check if the user has guessed correctly.
        if dashes == chosen_word:
            logging.info("""You Have Guessed the Correct Word
                         CONGRATULATIONS!! YOU HAVE WON THE GAME""")
            break
        else:
            continue
    else:
        logging.warning("sorry wrong guess.")
        CHANCES -= 1
        logging.info(dashes)
        #check if the user is out of chances
    if CHANCES == 0:
        logging.info(f"""SSORRY!! YOU LOST THE GAME
                     The Word Was: {chosen_word}""")
        break
                
