# Q-9

word = input("Enter word to search: ")

with open("sample.txt", "r") as f:
    lines = f.readlines()

found = False
for i, line in enumerate(lines, start=1):
    if word in line:
        print(f"Word found in line {i}")
        found = True

if not found:
    print("Word not found.")
