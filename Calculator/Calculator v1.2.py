calcList = []
signList = ['+', '-', '/', '*']

def numCheck(userInput):
    try:
        x = float(userInput)
        if x == int(x):
            return int(x)
        else:
            return x
    except ValueError:
        print("Numbers only please.")

def signCheck(userInput):
    try:
        sign = str(userInput)
        if sign in signList:
            return sign
        else:
            print('Enter a valid sign.')
    except ValueError:
        print('ValueError @signCheck')

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

tuna = 0
while True:
    if tuna == 0:
        numInput1 = input('Please enter a number: ')
        num1 = numCheck(numInput1)
        if num1 is not None:
            calcList.append(num1)
            tuna = 1
        else:
            print('Please enter a number')
            tuna = 0
    elif tuna == 1:
        signInput = input('Please enter a sign: ')
        sign = signCheck(signInput)
        if sign is not None:
            calcList.append(sign)
            tuna = 2
        else:
            print('Please enter a valid sign')
            tuna = 1
    elif tuna == 2:
        numInput2 = input('Please enter a number: ')
        num2 = numCheck(numInput2)
        if num2 is not None:
            calcList.append(num2)
            x, sign, y = calcList[0], calcList[1], calcList[2]
            if sign == '+':
                answer = add(x, y)
                print(answer)
                calcList = []
                calcList.append(answer)
                tuna = 1
            elif sign == '-':
                answer = subtract(x, y)
                print(answer)
                calcList = []
                calcList.append(answer)
                tuna = 1
            elif sign == '*':
                answer = multiply(x, y)
                print(answer)
                calcList = []
                calcList.append(answer)
                tuna = 1
            elif sign == '/':
                answer = divide(x, y)
                print(answer)
                calcList = []
                calcList.append(answer)
                tuna = 1