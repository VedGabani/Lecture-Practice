# Q-4

operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter first number -_- "))
num2 = float(input("Enter second number -_- "))

match operator:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    case _:
        print("Invalid operator entered.")
