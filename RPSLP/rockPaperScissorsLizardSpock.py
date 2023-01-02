player = input("Welcome! Let's play Rock, Paper, Scissors, Lizard, Spock. You have five lives. Press enter to start.")

from random import randint

t = ["rock", "paper", "scissors", "lizard", "spock"]

computer = t[randint(0,4)]

player = False

while player == False:

    lives = 5
    score = 0
    player = input("rock, paper, scissors, lizard, spock?")
    print("Computer plays",computer)
    if player == computer:
        print("Tie!")
        score + 1
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "lizard":
            print("You win!", player, "crushes", computer)
            score + 2
        elif computer == "spock":
            print("You lose!", computer, "vaporises", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        else:
            print("You win!", player, "smashes", computer)
            score + 2
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "lizard":
            print("You lose!", computer, "eats", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "spock":
            print("You win!", player, "disproves", computer)
            score + 2
        else:
            print("You win!", player, "covers", computer)
            score + 2
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "spock":
            print("You lose!", computer, "smashes", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "lizard":
            print("You win!", player, "decapitates", computer)
            score + 2
        else:
            print("You win!", player, "cuts", computer)
            score + 2
    elif player == "spock":
        if computer == "lizard":
            print("You lose!", computer, "poisons", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "scissors":
            print("You win!", player, "smashes", computer)
            score + 2
        elif computer == "rock":
            print("You win!", player, "vaporises", computer)
            score + 2
        else:
            print("You lose!", computer, "disproves", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
    elif player == "lizard":
        if computer == "spock":
            print("You win!", player, "poisons", computer)
            score + 2
        elif computer == "rock":
            print("You lose!", computer, "crushes", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
        elif computer == "paper":
            print("You win!", player, "eats", computer)
            score + 2
        else:
            print("You lose!", computer, "decapitates", player)
            lives - 1
            if lives == 0:
                print("Your socre is", score)
                break
    else:
        print("That's not a valid play!")
    player = False
    computer = t[randint(0,4)]