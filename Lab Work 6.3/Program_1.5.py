# Q-5

class InsufficientBalanceError(Exception):
    pass

balance = 10000000

def withdraw(amount):
    global balance

    if amount > balance:
        raise InsufficientBalanceError("You are poor")

    balance -= amount
    print("You got your money")
    print("Your left money -_- ", balance)

try:

    a = int(input("Enter a amount -_- "))
    withdraw(a)

except InsufficientBalanceError as e:

    print("Error -_- ", e)
