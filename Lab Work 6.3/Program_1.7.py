# Q-7

class InvalidGradeError(Exception):
    pass

try:

    grade = int(input("Enter a Grade -_- "))

    assert grade != "" , "Input can't be empty"

    if grade < 0 or grade > 100:

        raise ValueError("Must be b/w 0 to 100")

    if grade < 40:
        raise InvalidGradeError("Student Fail")
    print("Student pass")

except AssertionError as e:
    print("Assert -_- ", e)

except ValueError as e:
    print("Value -_- ", e)

except InvalidGradeError as e:
    print("Invalid Grade -_- ", e)
