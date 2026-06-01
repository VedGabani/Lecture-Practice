# Q-6

a = int(input("Enter a number to start a Triangle loop -_- "))
b = int(input("Enter a number to end a Triangle loop -_- "))

for i in range(b , a , -1):
    for j in range(1 , i - 1 , -1):
        print(j , end=" ")
    print()
