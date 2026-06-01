# Q-1

a = int(input("Enter a number to start a loop -_- "))
b = int(input("Enter a number to end a loop -_- "))

for i in range(a , b):
    if i % 4 == 0:
        continue
    print(i)
