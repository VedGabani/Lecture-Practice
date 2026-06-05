# Q-2

with open("sample.txt", "r") as f:
    print("Original Content:")
    print(f.read())

with open("sample.txt", "w") as f:
    f.write("Learning file handling in Python is fun!")

print("Content overwritten.")
