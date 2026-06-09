# Q-5

try:

    a = input("Enter a file name with extention -_- ")
    file = open(a , "r")
    print(file.read())

except FileNotFoundError:

    print("File not found")

finally:

    print("File is closed")
