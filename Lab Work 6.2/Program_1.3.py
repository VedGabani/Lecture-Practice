# Q-3

try:

    a = input("Enter a file name with extention -_- ")
    file = open(a , "r")
    

except FileNotFoundError:

    print("File not found")

else:

    print("Read done")
    print(file.read())
