import random

while True:
    user=input("rock scissors papper shoot:")

    if user=="scissors":
        if random.choice(["rock", "scissors", "paper"])=="scissors":
            print("tie")
        elif random.choice(["rock", "scissors", "paper"])=="rock":
            print("you lose")
        else:
            print("you win")

    if user=="rock":
        if random.choice(["rock", "scissors", "paper"])=="scissors":
            print("you win")
        elif random.choice(["rock", "scissors", "paper"])=="rock":
            print("tie")
        else:
            print("you lose")

    if user=="paper":
        if random.choice(["rock", "scissors", "paper"])=="scissors":
            print("you lose")
        elif random.choice(["rock", "scissors", "paper"])=="rock":
            print("you win")
        else:
            print("tie")
