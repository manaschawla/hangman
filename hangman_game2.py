"""this code is for hangman game in which you have to guess the word"""
import random
import logging
logging.basicConfig(level=logging.DEBUG)
WORDS = ["grace", "trust", "honor", "faith", "truth", "peace", "unity", "hope", "love",
         "care", "kind", "brave", "strong", "wise", "calm", "clear", "pure", "just", "fair", 
         "noble", "humble", "bright", "smart", "happy", "proud", "loyal", "honest", "joyful",
         "patient", "gentle", "bold", "calm", "vivid", "alert", "sharp", "keen", "quick", 
         "solid", "firm", "true", "grand", "good", "great", "worthy", "steady", "sound", "brisk",
         "swift", "free", "fresh", "kind", "mild", "rich", "wise", "calm", "deep", "calm", "calm",
         "sweet", "pure", "bright", "calm", "dear", "soft", "mild", "warm", "cool", "calm", "light",
         "high", "long", "wide", "deep", "full", "calm", "calm", "pure", "clean", "fine", "fair",
         "glad", "neat", "bright", "kind", "safe", "good", "pure", "fine", "fair", "neat", "calm",]
CHANCES = 5
logging.info(F"""WELCOME TO THE HANGMAN GAME.
             You Have To Guess the word correctly.
             you have {CHANCES} chances to guess the word correctly.""")
chosen_word = random.choice(WORDS)
logging.debug(f"the chosen word is : {chosen_word}")
word_length = len(chosen_word)
logging.debug(word_length)
dashes = '_' *  word_length
logging.info(dashes)
while True:
    print(f"you have chances left: {CHANCES}")
    guess = input("enter your guess: ")
    if guess in chosen_word:
        logging.info("you have guessed correct.")
        new_string = ""
        for index, charecter in enumerate(dashes):
            if guess == chosen_word[index]:
                new_string += chosen_word[index]
            else:
                new_string += dashes[index]
        dashes =  new_string
        print(dashes)
        if dashes == chosen_word:
            logging.info("CONGRATULATIONS!! YOU HAVE WON THE GAME")
            break
        else:
            continue
    else:
        logging.warning("sorry wrong guess.")
        CHANCES -= 1
        logging.info(dashes)
    if CHANCES == 0:
        logging.info(f"""SSORRY!! YOU LOST THE GAME
                     The Word Was: {chosen_word}""")
        break