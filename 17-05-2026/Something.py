'''
Array inside another arrays
Stires datta: Rows & Colums
It looks like a table or matrix
'''
arr1 = [1 , 2 , 3 , 4 , 5]
arr = [  [1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] ]

print(arr1)
print(arr)

'''
Accessing element in 2D array
Syntax -_- arry[rows][[column]
'''
print("\n")
print(arr1[0])
print(arr[0][0])

# Tking inpu t in 2D array

print("\n")

arr = []

rows = int(input("Enter rows -_- "))
col = int(input("Enter coloums -_- "))

print("\n")

for i in range(rows):
    row = []
    for j  in range(col):
        value = int(input(f"arr[{i}] [{j}] -_- "))
        row.append(value)
    arr.append(row)

print(arr)

# Printing 2D array using nested loop

arr = [  [1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] ]

for i in arr:
    for j in i:
        print(j , end = " ")
    print()

# Sum of all element in 2D array

total = 0

for i in arr:
    for j in i:
        total +=j
print("\nTotal -_- ", total)

# Syntax

num = [1,3,6,9,5]

num.sort()
print(num)
