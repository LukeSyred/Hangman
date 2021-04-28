# Import random and the word list

import random
words = open('sowpods.txt', 'r').readlines()

# Define word-choosing function

def choose_word():
    word = random.choice(words).strip()
    return word

# Initialise question for playing multiple times

qContinue = 'y'

# Start loop which allows multiple plays

while qContinue == 'y':

# Set word variable to be result of choose_word function, create a copy as
# orig_word, and a string of underscores the same length as the word

    word = choose_word()
    orig_word = word
    blanks = "_" * len(word)

# Turn the word and blanks into lists, and make a list of allowed characters, i.e.
# all letters.  Also make an empty list of guessed letters and set initial lives.

    word = list(word)
    blanks = list(blanks)
    allowed = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    lstGuessed = []
    lives = 10

# Print initial messages to player

    print("\nWelcome to Hangman!\n")
    print("You start with 10 lives.\n")

# Show the word to be guessed with blank letters

    print (" ".join(blanks), "\n")

# Main loop of game function.
# Runs until all underscores in blanks have been replaced by letters

    while "_" in blanks:

        guess = input("Guess a letter > ").upper() # The case of the user's guess doesn't matter

        if guess not in allowed:
            print("That's not a letter.\n")

        elif guess in lstGuessed or guess in blanks:
            print("\nAlready guessed!\n")
            print (" ".join(blanks),"\n")

# If guessed letter isn't in the word, add it to the list of guessed letters
# and subtract a life.

        elif guess not in word and guess not in lstGuessed:
            lstGuessed.append(guess)
            print("\nWRONG!\n")
            lives = lives-1
            if lives == 0:
                print("You lose!\n")
                print(f"It was {orig_word}.\n")
                break
            else:
                print(f"You have {lives} lives remaining.\n")
                print (" ".join(blanks),"\n")

# If the guess letter is in the word, change the corresponding underscore in blanks
# to that letter.

        else:
            print("\nThat's in the word!\n")
            while guess in word:
                index = word.index(guess)
                blanks[index] = guess
                word[index] = "_"
                print (" ".join(blanks),"\n")

                if "_" not in blanks: print ("You win!\n")

# Give user chance to end while loop
    qContinue = input("Would you like to play again? y/n")
