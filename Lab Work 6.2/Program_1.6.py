# Q-6

try:

    a = int(input("Enter a first number -_- "))
    b = int(input("Enter a first number -_- "))

    c = a/b

    print(c)

except ZeroDivisionError:

    print("You are 10th fail")

except ValueError:

    print("Alphabet can't divide")

finally:

    print("Program closed")
