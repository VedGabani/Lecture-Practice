# Q-6

class InvalidNameError(Exception):
    pass

def valid(email):
    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidNameError("Enter a proper Email address")

    print("Valid Emial")

try:

    a = input("Enter a Email -_- ")
    valid(a)

except InvalidNameError as e:
    print("Error -_- ", e)
