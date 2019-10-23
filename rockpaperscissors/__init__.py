from random import randint      #TODO: Change randint with choice

choices = ["rock", "paper", "scissor"]

def playRPS():
    comp_choice = choices[randint(0, 2)]
    user_choice = input("Rock, paper or scissor? ")
    if user_choice in choices:
        if user_choice != comp_choice:
            if user_choice == choices[0] and comp_choice == choices[1]:       # P: Rock, C: Paper
                print("Computer chose paper and you lost.")
            elif user_choice == choices[0] and comp_choice == choices[2]:      # P: Rock, C: Scissor
                print("You win!")
            elif user_choice == choices[1] and comp_choice == choices[0]:      # P: Paper, C: Rock
                print("You win!")
            elif user_choice == choices[1] and comp_choice == choices[2]:      # P: Paper, C: Scissor
                print("Computer chose scissors and you lost.")
            elif user_choice == choices[2] and comp_choice == choices[0]:      # P: Scissor, C: Rock
                print("Computer chose rock and you lost.")
            elif user_choice == choices[2] and comp_choice == choices[1]:      # P: Scissor, C: Paper
                print("You win!")
        else:
            print("Its a tie!")
    else:
        print("Unknown input")

while True:
    playRPS()