######################################################################
# FILE : hangman.py                                                  #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex4 2015-2016                                  #
# DESCRIPTION: The code below is made out of a few functions that    #
# using the hangman_helper file will let you play the hangman game   #
######################################################################
# importing the given hangman_helper
import hangman_helper


# a function that will update the word pattern with the given letter
def update_word_pattern(word, pattern, letter):
    # will run from 0 to the word length
    for i in range(len(word)):
        # checks if letter in index i in word is the letter and if it is it
        # will update the given pattern
        if word[i] == letter:
            pattern = pattern[:i] + letter + pattern[(i + 1):]
    # here we return the pattern if it was changed and if it remained the
    # same it will also return it
    return pattern


# this function runs a single game of hangman
def run_single_game(words_list):
    # here we create a random word from a given list using the helper
    word = hangman_helper.get_random_word(words_list)
    # here we create an empty guess list and a pattern which will be '_' the
    #  size of the word length and will create a guess counter that will
    # count how many guesses the user made
    guess_list = []
    pattern = '_' * len(word)
    guess = 0
    # creating a message with a defualt message given from the helper
    message = hangman_helper.DEFAULT_MSG
    # starting a loop that runs as long as the guess counter is lower then
    # the max errors generated from the helper file
    while hangman_helper.MAX_ERRORS > guess:
        # displaying the state of the game every time a new loop has started
        hangman_helper.display_state(pattern, guess, guess_list, message)
        # here we get the input for the first time and because the input is
        # a tuple we will divide it into intype(the type of the input) and
        # invalue which will be the value of the input
        (intype, invalue) = hangman_helper.get_input()
        # type =1 means the player wants a hint
        if intype == 1:
            words_list = filter_words_list(words_list, pattern, guess_list)
            message = hangman_helper.HINT_MSG + choose_letter(words_list,
                                                            pattern)
        # type =2 means the player entered a letter
        if intype == 2:
            # here we'll check if the letter is in fact one single letter and
            #  is lowercase
            if invalue.isalpha() is False or invalue.islower() is False or \
                    len(invalue) != 1:
                # if its not a single letter or its not a letter or not a
                # lowercase it will put a non-valid message into the message
                message = hangman_helper.NON_VALID_MSG
            # here it will check if the given letter is already in the
            # pattern or already in the list of guessed letters
            elif invalue in guess_list or invalue in pattern:
                # if the input is already in them it will put already chosen
                #  message into the message including what he typed
                message = hangman_helper.ALREADY_CHOSEN_MSG + invalue
            # checks if the given input is in the word which means its a
            # good guess and then it will use the first function which is
            # update_word_pattern to update the pattern with the new letter!
            # also we will reset the message into the default message
            elif invalue in word:
                pattern = update_word_pattern(word, pattern, invalue)
                message = hangman_helper.DEFAULT_MSG
            # if the letter is not in the word and isn't a wrong input and
            # wasn't guessed before then we'll put it into the letters guess
            # list raise the guess counter and will reset the message to the
            # default message
            else:
                guess_list.append(invalue)
                message = hangman_helper.DEFAULT_MSG
                guess += 1
            # here i'll check if the user guessed the word we'll do it in
            # the loop because if he guessed the word before he ran out of
            # guesses we want the loop to end and give him a win message and
            #  display a new state that will also ask him if he wants to
            # play again
            if pattern == word:
                message = hangman_helper.WIN_MSG
                hangman_helper.display_state(pattern, guess, guess_list,
                                             message, True)
                return
    # now if we got out of the loop it means the user lost the game and so
    # i'll put a loss message including the word that he was suppose to
    # guess into the message and display the state with the button that asks
    #  if he wants to play again
    message = hangman_helper.LOSS_MSG + word
    hangman_helper.display_state(pattern, guess, guess_list, message, True)


# this function will create a new list of words that have the same size as
# the pattern and the same letters that are shwon in the pattern not
# including the '_' of course
def filter_words_list(words, pattern, wrong_guess_list):
    # creating a newlst that will contain the new words list, i will save
    # the pattern length because i will use it more than once in this
    # function and i create a boolean that he's default will be true for the
    #  while we have in this function
    newlst = []
    pattlength = len(pattern)
    boolean = True
    # here we start the first loop that will run on every word from the
    # words list
    for word in words:
        # we'll check if the word has the same length as the pattern first
        # if so we'll continue to the while loop
        if len(word) is pattlength:
            # here i created another int called j so i can run on each letter
            # of the pattern and the word
            j = 0
            # a while that runs as long as my boolean is true and the
            # counter is smaller then the pattern length
            while boolean is True and j < pattlength:
                # if the letter in j index in pattern is a _ and if the word
                #  letter in index j is in the guess list already than we'll
                #  end the loop
                if pattern[j] == '_' and word[j] in wrong_guess_list:
                    boolean = False
                # here we check if the pattern and the word have different
                # letters and so we'll break the loop too
                if pattern[j] != word[j] and pattern[j] != '_':
                    boolean = False
                # if the letter was okay we will run for the next letter by
                # raising the counter j by 1
                j += 1
            # here we got out of the loop and if the boolean stayed True
            # than we will append the word to the newlst and then we will
            # run the while again by resetting the boolean to true
            if boolean is True:
                newlst.append(word)
            boolean = True
    # returning the new list of words
    return newlst

# here we create letter_to_index and index_to_letter from the given ex4.pdf
# in order to use them in our next function
__INIT_ALPHA_ORDER__ = 97


def letter_to_index(letter):
    """
    returns the index of a letter in an alphabet list
    """
    return ord(letter.lower()) - __INIT_ALPHA_ORDER__


def index_to_letter(index):
    """
    returns the index of the given letter in an alphabet list
    """
    return chr(index + __INIT_ALPHA_ORDER__)


# a function that gets a words list and a given pattern and will return the
# letter that repeats itself the most in the given list.
def choose_letter(words, pattern):
    # here we create a new list with the length of the alphabet and all of
    # the chars are now valued zero because we will count their appearance
    lettersinword = [0] * 26
    # a loop that runs for each word in words
    for word in words:
        # here we run a counter j in the range of the length pattern
        for j in range(len(pattern)):
            # checking if letter in index j of word is in pattern or not
            # if its not in the pattern than i will add +1 to its index in
            # the alphabet letters list or else it will continue running
            if word[j] not in pattern:
                lettersinword[letter_to_index(word[j])] += 1
    # when we get out of the loop the list will be with different integer
    # values for each word so we'll return the maximum value in the list
    # converted into a letter using index to letter
    return index_to_letter(lettersinword.index(max(lettersinword)))


# our main function that will run the game as long as the user wants to play
def main():
    # lodaing the words.txt into a list so we can work with the txt file
    wordlst = hangman_helper.load_words('words.txt')
    # running a single game using the word list
    run_single_game(wordlst)
    # here we finished a single game so we'll get a new input and we'll
    # check if the user wants to play again by checking if the intype(input
    # type) is 3 (play again type) and the value of it (invalue) is True
    (intype, invalue) = hangman_helper.get_input()
    if intype == 3 and invalue is True:
        run_single_game(wordlst)
    # if the user does not want to play again we will end the function thus
    # ending our program
    else:
        return

# a function that runs the gui for the main function and closes it when it
# finishes
if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()

