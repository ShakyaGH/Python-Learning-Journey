while True:

    print("Basic Calculator")
    print("Main Menu")
    print("1.addition(+) \n2.subtraction(-) \n3.division(/) \n4.multiplication(*) \n5.exponentiation(^) \n6.integer division(//) \n7.modulus division(%) \n8.Reset($) \n9.Exit")

    operator = input("Enter the symbol of an operator from the above list to begin the calculation: ")
    operator_list = ["+", "-", "*", "/", "^", "//", "%", "$", "X"]

    if operator == "X":
        print("Thank you")
        exit()

    if operator == "$":
        print("Calculator Reset")
        continue

    elif operator not in operator_list:
        print("Operator not in the list")
        continue

    else:
        try:
            a = input("Enter the first number: ")
            b = input("Enter the first number: ")
        except ValueError:
            print("Enter valid numbers")
            continue
        if "$" in [a, b]:
            print("Calculator Reset")
            continue
        if "X" in [a, b]:
            print("Thank you")
            exit()

        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print("Enter valid numbers")
            continue

        if operator == "+":
            r = a + b

        elif operator == "-":
            r = a - b

        elif operator == "/":
            if b == 0:
                print("Can't divide by zero")
                continue
            else:
                r = a / b

        elif operator == "*":
            r = a * b

        elif operator == "^":
            r = a ** b

        elif operator == "//":
            if b == 0:
                print("Can't divide by zero")
                continue
            else:
                r = a // b

        elif operator == "%":
            if b == 0:
                print("Can't divide by zero")
                continue
            else:
                r = a % b

        print(f"Answer = {r}")
