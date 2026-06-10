'''

Raise keyword

It is used to manually triger and exception in python

'''

age = 5

if age<0:

    raise ValueError("Can't be -ve")

'''

Assert Keyword

It is used to debugging and testing

'''

num = 10

assert num > 0 , "Num must be +ve"

print("Valid number")

# Custom exception

class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500

try:

    if withdraw > balance:
        raise InsufficientBalanceError("Not allowed")
    print("Withdraw done")

except InsufficientBalanceError as e:
    print("Error -_- ", e)
