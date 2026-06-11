# Q-4

def check(a):
    assert a != "" , "Enter a number or word"

    if a == a [:: -1]:
        print("Palindrome")

    else:
        print("Not Palindrome")


try:

    b = input("Enter a word -_- ")
    check(b)

except AssertionError as e:

    print("Error -_- ", e)
