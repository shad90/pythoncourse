# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # Defining a boolian vairbale to use as flag and Initializing
    # it as False
    notIn = False
    for l in secretWord:
    #If any single letter of secretWord is not in lettersGuessed
    #Function should return false.
        if l not in lettersGuessed:
    #Setting the variable notIn to True
            notIn = True
            #Don't need to remain in loop. So break out
            break

    if notIn == True: #all the letters of secretWord are not in lettersGuessed
        return False
    else: #all the letters of secretWord are in lettersGuessed
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ''
    for l in secretWord:
        if l in lettersGuessed:
            guessedWord += l
        else:
            guessedWord += '_'
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    ascii_list = list(string.ascii_lowercase)
    for l in lettersGuessed:
        if l in ascii_list:
            ascii_list.remove(l)
    return ''.join(ascii_list)

def alreadyGuessed(lettersGuessed,userGuess):
    '''
    input:(list, string), list: list of already guessed letters
                          string: character input from user
    userInput will update the list of guesses
    returns list of characters
    '''
    if userGuess in lettersGuessed:
        return True
    else:
        lettersGuessed.append(userGuess)
        return False
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    leftGuesses = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    while leftGuesses > 0:
        print("You have " + str(leftGuesses) + " guesses left")
        print("Available Letters:",getAvailableLetters(lettersGuessed) )
        userGuess = (input("Please guess a letter: ")).lower()
        if True == alreadyGuessed(lettersGuessed,userGuess):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
        elif userGuess in secretWord:
            print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
            if isWordGuessed(secretWord,lettersGuessed) == True:
                print("Congratulations, you won!")
                break
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
            leftGuesses -= 1
    if leftGuesses == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = 'hangman'
hangman(secretWord)
