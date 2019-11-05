from random import randint

def dice():
    while True:
        src = input('Do you want to roll the dice? (Y/N): ')
        if src.casefold() == 'y':
            diceFace = randint(1, 6)
            print('You rolled a dice and the result was: ', diceFace)
        elif src == 'N' or src == 'n':
            print("Thanks for using this silly code.")
            break
        else:
            print("Y/N input only please.")
            continue

dice()