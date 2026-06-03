# Q-2

def factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= 1
    return fact
num = int(input("Enter a number -_- "))
print("Factorial -_- ", factorial(num))
