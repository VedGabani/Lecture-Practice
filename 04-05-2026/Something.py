# Built in function v/s user defined function (UDF)
# Built in function

numbers = [10, 20, 30, 40]

print("Length -_- ", len(numbers))
print("Max -_- ", max(numbers))
print("Min -_- ", min(numbers))

# These are pre-defined function inside python and you don't need to create them

# UDF

def greet(name):
    return "Hello" + name
print(greet ("Ved"))
print(greet ("Vraj"))

# you defined this function using def
# Arbitartry Arguments
# When number of input is unknown

def add_num(*args):
    total = 0
    for num in args:
        total += num
        return total

print(add_num(1, 2, 3, 4, 5, 6))

# keyword Argument (**kwargs)
# Whe passed in name value

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key ,":", value)

student_info(name = "Ved", age =17, course = "Python")

# **kwargs store data in a dictionary
# doc (document string)
# used to describe function

def  mutiply(a,b):
    """ This function return the multiplication of  2 number """
    return a*b

print(mutiply (10,10))
print(mutiply.__doc__)
