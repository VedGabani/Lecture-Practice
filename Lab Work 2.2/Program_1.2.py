# Q-2

a = int(input("\nEnter First Number -_- "))
b = int(input("\nEnter Second Number -_- "))
c = int(input("\nEnter Third Number -_- "))

if a<b and a<c:
    print("\nFirst Number is Smallest")

elif b<a and b<c:
    print("\nSecond Number is Smallest")

elif c<a and c<b:
    print("\nThird Number is Smallest")

else:
    print("\nAll Number is Same")
