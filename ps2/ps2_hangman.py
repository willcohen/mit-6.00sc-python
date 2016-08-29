# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


def intro(secret):
    """
    Returns opening instructions to player.
    """
    return 1


def available_letters(remaining, guess):
    """
    Check for available letters.
    """
    newstr = ""
    for i in remaining:
        # print i
        # print "Checking " + i
        if i == guess:
            # print "removing ", guess
            # print "new string: ", newstr
            newstr
        else:
            newstr = newstr + i
            # print "new string: ", newstr
    return newstr


def guess_test(secret, guess, guessed):
    """
    Check the guess.
    """
    hidden = ''
    global guesses
    for l in secret:
        if l in guessed:
            hidden = hidden + l
        else:
            hidden = hidden + '_'
    if guess in secret:
        print "Good guess: " + hidden
    else:
        print "Oops! That letter is not in my word: " + hidden
        guesses += -1
    if '_' not in hidden:
        print "Congratulations, you won!"
        return
    return ""


def hangman():
    """
    Plays the game hangman.
    """
    secret = choose_word(wordlist)
    global guesses

    print "I am thinking of a word that is " + str(len(secret)) + \
        " letters long."
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    alphabet = ''.join(alphabet)
    guessed = []
    remaining = alphabet[:]
    guess = ''
    global guesses
    guesses = 8
    while guesses > 0:
        print 'You have ' + str(guesses) + " guesses left."
        remaining = available_letters(remaining, guess)
        print 'Available letters: ' + ''.join(remaining)
        guess = str(raw_input('''Please guess a letter: '''))
        guessed.append(guess)
        print ''.join(guessed)
        hidden = ''
        for l in secret:
            if l in guessed:
                hidden = hidden + l
            else:
                hidden = hidden + '_'
        if guess in secret:
            print "Good guess: " + hidden
        else:
            print "Oops! That letter is not in my word: " + hidden
            guesses += -1
        if '_' not in hidden:
            print "Congratulations, you won!"
            break
    if guesses == 0:
        print "You are out of guesses."

    return
