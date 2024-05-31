import random

def game():
    while True:
        Choices = ["ROCK", "PAPER", "SCISSOR"]
        print("EXIT")
        print(Choices)
        Player = input("Enter Your Choice : ").upper()
        if Player == "EXIT":
            print("Exiting the game...")
            break
        elif Player not in Choices:
            print("Enter Correctly")
            continue
        Bot = random.choice(Choices)
        print("Your Choice is : ", Player)
        print("Bot Choice is  : ", Bot)
        if Player == Bot:
            print("Match Die")
        elif (Player == "ROCK" and Bot == "SCISSOR") or \
             (Player == "PAPER" and Bot == "ROCK") or  \
             (Player == "SCISSOR" and Bot == "PAPER"):
            print("You Win.........")
        elif Player == "EXIT":
            break
        else:
            print("Bot Wins.........")

game()
