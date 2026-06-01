# Q-7

for i in range(1, 51):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "- Divisible by both")
    elif i % 2 == 0:
        print(i, "- Divisible by 2")
    elif i % 3 == 0:
        print(i, "- Divisible by 3")
