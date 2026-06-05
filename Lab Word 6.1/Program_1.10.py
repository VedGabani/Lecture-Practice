# Q-10

with open("source.txt", "r") as src:
    content = src.read()

with open("backup.txt", "w") as dest:
    dest.write(content)

print("File copied successfully.")
