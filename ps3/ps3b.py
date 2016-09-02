from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    topword = ''
    topscore = 0
    for i in range(1, HAND_SIZE):
        for j in get_perms(hand, i):
            if is_valid_word(j, hand, word_list):
                #print 'Valid word: ', j, ', ', get_word_score(j, HAND_SIZE)
                if get_word_score(j, HAND_SIZE) > topscore:
                    topscore = get_word_score(j, HAND_SIZE)
                    topword = j
                    #print 'Tentative choice: ', topword, ' ', topscore
    return topword

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    temphand = hand.copy()
    word = ' '
    totalscore = 0
    print 'Initial hand: ', display_hand(temphand)
    while word != '':
        word = comp_choose_word(temphand, word_list)
        score = get_word_score(word, HAND_SIZE)
        temphand = update_hand(temphand, word)
        if word != '':
            print '"'+word+'" earned ', score, ' points.'
            totalscore += score
            print 'Total score: ', totalscore
        print 'Remaining hand: ', display_hand(temphand)
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    userchoice = ''
    playerchoice =''
    hand = {}
    while playerchoice != 'u' or playerchoice != 'c':
        playerchoice = raw_input("""Input 'u' to play a hand yourself. \
Input 'c' to make the computer play: """)
        if playerchoice == 'u':
            while userchoice != 'e':
                userchoice = raw_input("""Input 'n' to play a new hand. \
Input 'r' to play the last hand again. Input 'e' to exit: """)
                if userchoice == 'e':
                    return
                if userchoice == 'n':
                    hand = deal_hand(HAND_SIZE)
                    play_hand(hand, word_list)
                if userchoice == 'r':
                    play_hand(hand, word_list)
        if playerchoice == 'c':
            hand = deal_hand(HAND_SIZE)
            comp_play_hand(hand, word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
