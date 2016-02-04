from nltk.tokenize import RegexpTokenizer
import random
import sys
import os


def begin():
    # Player begins and chooses a difficutly
    difficutly = input("Welcome to Mystery Word! (A knock off of hangman!) "
                       "Choose your difficutly, [E]asy, [M]edium, [H]ard "
                       "Typer the letter in the bracket. ").lower()
    if difficutly == 'e':
        secret_word = easy_word()
        return gen_board(secret_word)


def easy_word():
    word = gen_random_word(4, 6)
    return word

def gen_random_word(min_letter, max_letter):
    # Generate the word from the words file on pc
    with open('/usr/share/dict/words') as f:
        # Normalize text and pick work
        text = f.read()
        tokenizer = RegexpTokenizer(r'\w+')
        content = tokenizer.tokenize(text)
        words = [word.lower() for word in content if min_letter <= len(word) <= max_letter]
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
    # Allow player to guess
    while len(bad_guesses) < 7:
        guess = display(bad_guesses)
        if guess in good_guesses:
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
    bad_guesses.append(guess)
    bad_guesses = ''.join(bad_guesses)
    clear()
    print(board)
    return board

def same_guess(board):
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

begin()