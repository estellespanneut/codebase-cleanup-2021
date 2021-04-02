
from random import choice

#
# USER SELECTION
#
valid_options = ["rock", "paper", "scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_options:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

def determine_winner(u):
    if u == "rock":
        if c == "rock":
            print("It's a tie!")
        elif c == "paper":
            print("The computer wins")
        elif c == "scissors":
            print("The user wins")
    elif u == "paper":
        if c == "rock":
            print("The user wins")
        elif c == "paper":
            print("It's a tie!")
        elif c == "scissors":
            print("The computer wins")
    elif u == "scissors":
        if c == "rock":
            print("The computer wins")
        elif c == "paper":
            print("The user wins")
        elif c == "scissors":
            print("It's a tie!")

determine_winner(u)