# Q-1

def check_even():

    num = int(input("Enter a number -_- "))

    if not isinstance(num , int):
        raise TypeError ("Input must be an integer")

    if num % 2 != 0:
        raise ValueError ("\nNumber is odd")
    print("\nNumber is even")

try:

    check_even()

except Exception as e:

    print("\nError -_- ", e)

except ValueError:

    print("\nOnly numbers")
