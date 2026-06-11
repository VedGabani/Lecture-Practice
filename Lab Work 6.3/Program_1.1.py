# Q-1

try:

    num = int(input("Enter a number -_- "))

    if num < 0:
        raise ValueError("Number must be positive")
    print("You got it")

except ValueError as e:
    print("Error -_- ", e)
