# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------

#game uses pre-set dictionary of choosing called "words.txt"
def hangman(turns):
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

    wordlist = load_words()

    # choose word and set-up
    word = choose_word(wordlist)
    wordlength = len(word)

    #create blank schema to fill
    blanks = str(" _ ")*wordlength
    
    #create function for filling blank schema
    bl = []
    for i in range(1,3*wordlength, 3):
        bl += blanks[i]

    def fill_word(letter):
        """
        letter (string): letter as chosen by player

        fills blanks string with instances of chosen letter
        """
        for i in range(0, wordlength):
            if word[i] == letter:
                bl[i] = letter
        return ' '.join(map(str, bl))

    alphabet = string.ascii_lowercase
    print "Welcome the game, Hangman!"
    print "I am thinking of a word that is " + str(wordlength) + " letters long!"
    print blanks
    guesses = turns
    letter = ""
    while guesses >= 1 and "_" in fill_word(letter):
        print "You have " + str(guesses) + " guess(es) left."
        print "Available letters: " +str(alphabet)
        letter = str(raw_input('Please guess a letter:'))
        if letter in word:
            print "Good guess: " +str(fill_word(letter))
        else:    
            print "Oops! That letter is not in my word: " +str(fill_word(letter))
            guesses -=1
        alphabet = alphabet.replace(letter,"")

    if "_" in fill_word(letter):
        print "Sorry, you are out of guesses. =("
        print "My word was " + str(word) + "."
    else:
        print "Congratulations! You guessed my word!"
     
        








    
    
