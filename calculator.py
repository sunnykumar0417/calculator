try:
    num1 = float(input("Enter your first number: "))
    op = input("Please choose the operator from +, -, *, /, **: ")
    num2 = float(input("Enter your second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    elif op == '**':
        print("Result:", num1 ** num2)
    else:
        print("Invalid operator.")
except ValueError:
    print("Invalid number entered.")
