
from random import randint

def userInput():
    while True:
        src = input("Do you want to play? (Y/N)")
        if src == "Y" or src == "y" or src == "1":
            print("Great! You have 5 chances to pick a number between 1 and 20.")
            numGuesser(randint(1, 20))
        elif src == "N" or src == "n" or src == "0":
            exit()
        else:
            print("Unknown input, please try again.")
            continue

def numGuesser(num):
    counter = 5
    while True:
        try:
            guess = int(input("Your guess: "))
            if 1 <= guess <= 20:
                print("ASSERT")
                if guess == num:
                    print("Correct!")
                elif guess != num:
                    counter -= 1
                    if counter == 0:
                        print("You lost!")
                        userInput()
                    else:
                        continue
            else:
                print("Error")
        except ValueError:
            print("Please enter a number between 1 and 20.")
            continue

userInput()