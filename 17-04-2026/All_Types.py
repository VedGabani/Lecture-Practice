# Python Variable Datatype and Operators
# Variable Assigment
x = 5
y = "How are you"
z = 20.20

'''

Variable Naming Rule
Must start with a letter and underscore
cannot start with number

12 = "Hello"
12demo = 3.14

can only contain alpha-numeric character and underscore

'''

name20 = "Ved Gabani"
print(name20)

'''

Case sensitive language
age,Age,aGe,agE,AGE are different variables

'''

my_var = "Hello World"
_var = 25

print(my_var)
print(_var)

'''

Data Types
Python has several built in Data types

1) Basic types
2) Numeric types

demo = 20 (int)
demo1 = 20.20 (float)
demo2 = 3+2i (complex)

Text type

name = "Hello World" (string)
Boolean Type
bool: True and False

'''

a = 10
print("Type of a -_- ",type(a))

b = "Hello"
print("Type of b -_- ",type(b))

c = True
print("Type of c -_- ",type(c))

'''

List Types Datat
1) List of python
2) Tuple
3) Set
4) Dict

Python operators

1) Arithmetic Operator
2) Assigment Operator
3) Comperison Operator
4) Logical Operator
5) Membership Operator
6) Identity Operator

'''

# 1) Arithmetic Operator

a = int(input("Enter First Number -_- "))
b = int(input("Enter Second Number -_- "))

print("Addition is -_- ", a+b)
print("Subtraction is -_- ", a-b)
print("Division is -_- ", a/b)
print("Multiplicaton is -_- ", a*b)
print ("Modulus -_- ", a%b)
print("Expontiation -_- ", a**b)
print("Floor Division -_- ", a//b)

# 2) Assigment operator

x = int(input("Enter First Number -_- "))
y = int(input("Enter Second Number -_- "))

x+=y
print("+= -_- ", x) # x=x+y

x-=y
print("-= -_- ", x) # x=x-y

x*=y
print("*= -_- ", x) # x=x*y
 
x/=y
print("/= -_- ", x) # x=x/y

x%=y
print("%= -_- ", x) # x=x%y
print("%= -_- ", y) # y=x%y

y**=x
print("**= -_- ",y) # y=y**x

# 3) Comperrision operator

x = int(input("Enter First Number -_- "))
y = int(input("Enter Second Number -_- "))

print("Equal -_- ", x==y)
print("Not Equal -_- ", x!=y)
print("Greater than -_- ", x>y)
print("Less than -_- ", x<y)
print("Greater than and equal -_- ", x>=y)
print("Less than and equal -_- ", x<=y)

# 4) Logical operator

a = True
b = False

print("And -_- ", a and b)
print("Or -_- ", a or b)
print("Not -_- ", not a)
