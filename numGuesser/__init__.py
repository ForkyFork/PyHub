#? Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.

from random import randint

print("A random number was generated from 0 to 20. Guess that number!")

def srcInput():
    while True:
        try:
            userInput = int(input("Enter a number: "))
            if userInput < 0 or userInput > 20:
                print("Only numbers between 0 and 20.")
            else:
                numGuesser(userInput, randint(0, 20))
        except ValueError:
            print("Only numbers are allowed.")
            continue

def numGuesser(user_input, rand_number):
    if user_input < rand_number:
        print("Your guess is too low. The number was: ", rand_number)
    elif user_input > rand_number:
        print("Your guess is too high. The number was: ", rand_number)
    else:
        print("You guessed correctly!)

srcInput()