while True:
    print("Options:\n Use 'Add' to add two numbers.\n Use 'Sub' to subtract two numbers.\n "
          "Use 'Mult' to multiply two numbers.\n Use 'Div' to divide two numbers.\n Use 'Quit' to exit the program.")
    src_input = input("Please enter a command: ")
    if src_input == "Quit" or src_input == "quit":
        break
    elif src_input == "Add" or src_input == "add":
        try: 
            x = float(input("Please enter a number: "))
            y = float(input("Please enter another number: "))
            sum = str(x+y)
            print("The result is: " + sum)
        except ValueError:
            print("Wrong syntax, numbers only allowed.")
            continue
    elif src_input == "Sub" or src_input == "sub":
        try:
            x = float(input("Please enter a number: "))
            y = float(input("Please enter another number: "))
            sub = str(x-y)
            print("The result is: " + sub)
        except ValueError:
            print("Wrong syntax, numbers only allowed.")
            continue
    elif src_input == "Mult" or src_input == "mult":
        try: 
            x = float(input("Please enter a number: "))
            y = float(input("Please enter another number: "))
            prod = str(x*y)
            print("The result is: " + prod)
        except ValueError:
            print("Wrong syntax, numbers only allowed.")
            continue
    elif src_input == "Div" or src_input == "div":
        try: 
            x = float(input("Please enter a number: "))
            y = float(input("Please enter another number: "))
            if y == 0:
                print("You can't divide by zero.")
                continue
            else:
                div = str(x/y)
                print("The result is: " + div)
        except ValueError:
            print("Wrong syntax, numbers only allowed.")
            continue
    else:
        print("Please enter a valid command.")