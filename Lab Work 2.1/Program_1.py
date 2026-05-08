# Lab Work 2.1

# Q-1

a = int(input("\nEnter a number to check Even or Odd -_- "))

if a%2==0:
    print("\n The Number is Even")

else:
    print("The number is Odd")


# Q-2

a = int(input("\nEnter Your Age -_- "))

if a <= 12:
    print("\nYou are Child")

elif a<=19:
    print("\nYou are Teenager")

elif a<=59:
    print("\nYou are Adult")

else:
    print("\nYou are Senior")


# Q-3

a = int(input("\nEnter First Number -_- "))
b = int(input("\nEnter Second Number -_- "))
c = int(input("\nEnter Third Number -_- "))

if a>b and a>c:
    print("\nFirst Number is Greatest")

elif b>a and b>c:
    print("\nSecond Number is Greatest")

elif c>a and c>b:
    print("\nThird Number is Greatest")

else:
    print("\nAll Number is Same")
    
# Q-4

a = int(input("\n Enter a Number -_- "))

if a >= 0 and a % 1 == 0:
    print("\nThe Number is Natural")

else:
    print("\nThe is not a Natural Number")
