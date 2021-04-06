
from random import choice

#
# USER SELECTION
#
valid_options = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Params:
        choice1 and choice2 are both string : one of "rock", "paper", or "scissors"
    """
    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice


if __name__ == "__main__":

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
    winner = determine_winner(u, c)
    if winner == u:
        print("YOU WON!")
    elif winner == c:
        print("COMPUTER WON!")
    elif winner == None:
        print("TIE")

    def determine_winner1(u):
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

    #ATTRIBUTION: Lots of help and text was taken from class lectures
