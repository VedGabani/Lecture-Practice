# Q-2

try:

    age = int(input("Enter your age -_- "))

    assert age> 18 , "Age must be above 18"

    print("Valid age")

except AssertionError as e:

    print("Error -_- ", e)
