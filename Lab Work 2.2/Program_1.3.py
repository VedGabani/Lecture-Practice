# Q-3

a = int(input("\nEnter First Number -_- "))
b = int(input("\nEnter Second Number -_- "))
c = int(input("\nEnter Third Number -_- "))
d = int(input("\nEnter Third Number -_- "))

if a>b and a>c and a>d:
    print("\nFirst Number is Greatest")

elif b>a and b>c and b>d:
    print("\nSecond Number is Greatest")

elif c>a and c>b and c>d:
    print("\nThird Number is Greatest")

elif d>a and d>b and d>c:
    print("\nThird Number is Greatest")

else:
    print("\nAll Number is Same")
