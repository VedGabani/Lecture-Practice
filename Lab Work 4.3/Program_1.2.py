# Q-2

arr = []
size = int(input("Enter a range -_- "))
print("\n")

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

sum = 0

for i in arr:
    sum += i

print("\n",arr)
print("\n",sum)
