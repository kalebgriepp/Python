import random

print('Kaleb Griepp CSCI135 rock paper scissors')

options = ["rock", "paper", "scissors"]
opponent = random.choice(options)
program = False

while not program:
    player = str(input("\nEnter either rock, paper, or scissors(MUST be lower-case only): "))
    print("You:", player)
    if player == opponent:
        print("Computer chose: ", str(opponent))
        print("Tie!")
    elif player == "rock":
        if opponent == options[1]:
            print("Computer chose: ", str(opponent))
            print("You lose!", options[1], "covers", player)
        else:
            print("Computer chose: ", str(opponent))
            print("You win!", player, "smashes", options[2])
    elif player == "paper":
        if opponent == options[2]:
            print("Computer chose: ", str(opponent))
            print("You lose!", options[2], "cuts", player)
        else:
            print("Computer chose: ", str(opponent))
            print("You win!", player, "covers", options[0])
    elif player == "scissors":
        if opponent == options[0]:
            print("Computer chose: ", str(opponent))
            print("You lose!", options[0], "smashes", player)
        else:
            print("Computer chose: ", str(opponent))
            print("You win!", player, "cuts", options[1])
    else:
        print("Invalid Entry. Please try again.")
    program = False
    opponent = random.choice(options)