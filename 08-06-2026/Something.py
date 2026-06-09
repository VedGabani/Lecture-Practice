'''

An exception is an error that occurs during
program exception if on exception is not
handeled the proggram stop immediatly

To avoid program crashes python provide
exception handling using

try , catch ,  else , finally

1. try ..... except

'''

try:

    num = int(input("Enter a number -_- "))
    a = 10/num

except ZeroDivisionError:

    print("\nYou are 10th fail")

except ValueError:

    print("\nYou are 10th fail")

# 2. try ..... except ..... else

try:

    num = int(input("Enter a number -_- "))
    print(10/num)

except ZeroDivisionError:

    print("\nYou are 10th fail")

else:

    print(a)

# 3. try ..... except ..... finally

try:

    file = open("demo.txt" , "r")
    print(file.read())

except FileNotFoundError:

    print("\nfile not found")

finally:

    print("Progran closed")

# 4. try ..... except ..... else ..... finally

try:

    num = int(input("Enter a number -_- "))
    a = 10/num

except ZeroDivisionError:

    print("\nYou are 10th fail")

else:

    print(a)

finally:

    print("Program closed")
