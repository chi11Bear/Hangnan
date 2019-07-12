# Hangman
# Author - Darren Joyner


import sys
import random
   
def menu():
    easy = False
    hint = None
    print("Welcome to Hangman")
    print("\n")
    msg4 = ("One player (1) or Two players (2): ")
    print("\n")
    m = input(msg4)
    
    if (m == '1'):
        msg5 = ("would u like hints? (y/n): ")
        a = input(msg5)
        if a == 'y':
            easy = True
            
        ans = random.choice(myList)
        hangman(ans, hint, easy)
    elif (m == '2'):
        print("\n")
        msg3 = ("Player 2, pick a Mystery Word (NO SPACES): ")
        word = input(msg3)
        msg4 = ("Any hint? Type it in or hit Enter for no hint: ")
        hint = input(msg4)
        if (not(hint and hint.strip())):
            easy = False
        else:
            easy = True
        hangman(word, hint, easy)
    else:
        menu() 

def hangman(word, hint, easy):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    
    while wrong < len(stages)-1:
        print("\n")
        if easy == True:
            if word == "dog":
                hint = "Man best friend"
                print(hint)
            elif word == "knife":
                hint = "A tool use in the kitchen"
                print(hint)
            elif word == "chip":
                hint = "Perfect food for dip"
                print(hint)
            elif word == "oxygen":
                hint = "We all need it"
                print(hint)
            elif word == "sphinx":
                hint = "A famous statue"
                print(hint)
            elif word == "yacht":
                hint = "A personal cruise ship"
                print(hint)
            else:
                print(hint)
        
        msg = "Guess a letter: "
        char = input(msg).lower()

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0 : e]))
        if "_" not in board:
            print("\n")
            print("You Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n")
        print("\n".join(stages[0 : wrong]))
        print("You lose! It was {}.".format(word))

    print("\n")
    msg2 = "Would you like to play again? (y/n): " 
    char2 = input(msg2)
    print("\n")
    
    if char2 != 'n':
        menu()
    else:
        sys.exit()

myList = ["dog","knife","chip","oxygen","sphinx","yacht",]
        
menu()     
