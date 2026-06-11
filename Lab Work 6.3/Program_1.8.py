# Q-8

class HighTemperatureError(Exception):
    pass

try:

    temp = float(input("Enter Temperature -_- "))

    if not isinstance(temp , (int , float)):
        raise TypeError("Temp must be a number")


    assert -273 <= temp <= 10000("Temp out of range")

    if temp > 1000:
        raise HighTemperatureError ("Temp exceed 1000")

    print("Valid Temp -_- " , temp , "C")

except TypeError as e:
    print("Type Error -_- ", e)

except AssertionError as e:
    print("Assertion Error -_- ", e)

except HighTemperatureError as e:
    print("High Error -_- ", e)
