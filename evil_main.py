from nltk.tokenize import RegexpTokenizer
import random
import math
import pdb
import sys
import os


def begin():
    # Player begins the nightmare
    print("Welcome to nightmare mode of hangman! Think you have what it takes? "
          "Lets find out!")
    secret_word = gen_random_word()
    return gen_board(secret_word)

def gen_random_word():
    # Generate the word from the words file on pc
    with open('/usr/share/dict/words') as f:
        # Normalize text and pick work
        text = f.read()
        tokenizer = RegexpTokenizer(r'\w+')
        content = tokenizer.tokenize(text)
        words = [word.lower() for word in content if len(word) != 1]
        return words

def shuffle_word(letters):
    # Shuffle the word to another word with same correct letters
    with open('/usr/share/dict/words') as f:
        # Normalize text and pick work
        text = f.read()
        tokenizer = RegexpTokenizer(r'\w+')
        content = tokenizer.tokenize(text)
        words = [word.lower() for word in content if word in letters]
        word = random.choice(words)
        return word

def clear():
    # Clear the screen for easier readability
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def gen_board(secret_word):
    # Generate board 
    good_guesses = list(secret_word)
    bad_guesses = []
    board = len(good_guesses) * '_'
    board = list(board)
    board = ''.join(board)
    print("The length of the word is {} long".format(len(board)))
    print(board)
    return guess(secret_word, good_guesses, bad_guesses, board)
    
def guess(secret_word, good_guesses, bad_guesses, board):
    # Allow player to guess and display appropriate response
    correct_guesses = []
    good_guesses = list(secret_word)
    while len(bad_guesses) < 7:
        print(secret_word)
        guess = display(bad_guesses)
        if guess in good_guesses:
            board = list(board)
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    board[index] = letter
                    correct_guesses.append(guess)
            board = ''.join(board)
            clear()
            # If no more blanks player wins
            if '_' not in board:
                return player_win(secret_word)
            else:
                print(board)
        elif not guess.isalpha():
            not_letter(board)
        elif len(guess) != 1:
            too_many_letters(board)
        elif guess in bad_guesses:
            same_guess(board)
        else:
            add_bad_guess(guess, bad_guesses, board)
    else:
        player_loses(secret_word) 

def display(bad_guesses):
    # Display the board and bad guessed taken to the user
    bad_guesses = ''.join(bad_guesses)
    print("Strikes {}/10             {}\n".format(len(bad_guesses), (bad_guesses + ' ')))
    bad_guesses = list(bad_guesses)
    return input("Guess a letter ").lower()

def add_bad_guess(guess, bad_guesses, board):
    # Add the bad guess to list of bad guesses
    bad_guesses.append(guess)
    bad_guesses = ''.join(bad_guesses)
    clear()
    print(board)
    return board

def same_guess(board):
    # Display message player has already used that word
    print("You have already tried that letter! Try a different letter. \n")
    print(board)
    return board

def not_letter(board):
    # Display message if input is not letter
    print("That is a not a letter! Please type a letter. \n")
    print(board)
    return board

def too_many_letters(board):
    # Display message user put more than one letter
    print("You put more than one letter! Only put one letter \n")
    print(board)
    return board

def player_win(secret_word):
    # Player wins
    print("You win! The secret word was {}".format(secret_word))
    return play_again()

def player_loses(secret_word):
    # Player loses
    print("You lost! My secret word was {}".format(secret_word))
    return play_again() 

def play_again():
    # Allow player to play again if so chooses     
    again = input("Play again? Y/n ").lower()
    if again != 'n':
        return begin()
    else:
        sys.exit()






'''['dog', 'apple', 'banana', 'coconut', 'pear', 'peach', 'ukulele',
              'milk', 'eggs', 'while', 'color', 'blue', 'red', 'green', 'purple',
              'man', 'woman', 'animal', 'thing', 'anaconda', 'alzheimers', 'and', 'allily',
              'abomindiable']'''




def evil():
    # Create new board and new word but include correct letters player has given
    test_words = gen_random_word()
    secret_word = random.choice(test_words)
    board = '_' * len(secret_word)
    print(board)
    guess = input('Guess ')
    new_list = [word for word in test_words if guess not in word]
    back_up_list = new_list
    guesses = 1
    secret_word = random.choice(new_list)
    board = '_' * len(secret_word)
    print("Wrong!")
    print(board)
    while guesses < 15:
        guess = input('Guess ')
        if guess in secret_word:
            try:
                new_list = [word for word in new_list if guess not in word]
                secret_word = random.choice(new_list)
                board = '_' * len(secret_word)
                print("Wrong!")
                print(board)
                guesses += 1
            except (ValueError, IndexError):
                secret_word = secret_word
                print("Correct!")
                for index, letter in enumerate(secret_word):
                    if letter == guess:
                        board = list(board)
                        board[index] = letter
                        board = ''.join(board)
                print(board)
                while guesses < 15:
                    guess = input('Guess ')
                    if guess in secret_word:
                        for index, letter in enumerate(secret_word):
                            if letter == guess:
                                board = list(board)
                                board[index] = letter
                                board = ''.join(board)
                        print(board)
                        if '_' not in board:
                            print("You win!")
                            return sys.exit()
                    else:
                        print("Wrong!")
                        guesses += 1
        else:
            print("Wrong!")
            guesses += 1

evil()








