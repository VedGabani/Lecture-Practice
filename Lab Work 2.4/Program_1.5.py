# Q-5

a = int(input("Enter a number to start a Triangle loop -_- "))
b = int(input("Enter a number to end a Triangle loop -_- "))

for i in range(a , b):
    for j in range(1 , i + 1):
        print(j , end=" ")
    print()
