from nltk.tokenize import RegexpTokenizer
import random
import sys
import os


def gen_random_word():
    # Generate the word from the words file on pc
    with open('/usr/share/dict/words') as f:
        # Normalize text and pick work
        text = f.read()
        tokenizer = RegexpTokenizer(r'\w+')
        content = tokenizer.tokenize(text)
        words = [word.lower() for word in content]
        word = random.choice(words)
        return word

def clear():
    # Clear the screen for easier readability
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def gen_board():
    # Generate board 
    secret_word = gen_random_word()
    good_guesses = list(secret_word)
    bad_guesses = []
    board = len(good_guesses) * '_'
    board = list(board)
    board = ''.join(board)
    print("The length of the word is {} long".format(len(board)))
    print(board)
    return guess(secret_word, good_guesses, bad_guesses, board)
    
def guess(secret_word, good_guesses, bad_guesses, board):
    # Allow player to guess
    while len(bad_guesses) < 9:
        bad_guesses = ''.join(bad_guesses)
        print("Strikes {}/10             {}".format(len(bad_guesses), (bad_guesses + ' ')))
        bad_guesses = list(bad_guesses)
        print(secret_word)
        guess = input("Guess a letter ")
        if guess == 'Q':
            return exit()
        elif guess in good_guesses:
            board = list(board)
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    board[index] = letter
            board = ''.join(board)
            clear()
            # If no more blanks player wins
            if '_' not in board:
                return player_win(secret_word)
            else:
                print(board)
        elif not guess.isalpha():
            not_letter()
        elif guess in bad_guesses:
            print("You have already tried that letter! Try a different letter. \n")
            print(board)
        else:
            bad_guesses.append(guess)
            bad_guesses = ''.join(bad_guesses)
            clear()
            print(board)
            bad_guesses = list(bad_guesses)
    else:
        print("You lost! My secret word was {}".format(secret_word))
        return play_again()  

def not_letter(board):
    # Display message if input is not letter
    print("That is a not a letter! Please type a letter. \n")
    return board

def player_win(secret_word):
    # Player wins
    print("You win! The secret word was {}".format(secret_word))
    return play_again()

def exit():
    # Exit game
    print("Thanks for playing!")
    return sys.exit()

def play_again():
    # Allow player to play again if so chooses     
    again = input("Play again? Y/n ").lower()
    if again != 'n':
        return gen_board()
    else:
        sys.exit()
        
gen_board()