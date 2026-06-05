# Q-11

with open("demo.txt", "w") as f:
    f.write("Initial Content\n")

with open("demo.txt", "r") as f:
    print("Read (r):", f.read())

with open("demo.txt", "w") as f:
    f.write("Overwritten Content\n")

with open("demo.txt", "a") as f:
    f.write("Appended Content\n")

with open("demo.txt", "r+") as f:
    print("Read+Write (r+):", f.read())
    f.write("Added using r+\n")

with open("demo.txt", "w+") as f:
    f.write("Written using w+\n")
    f.seek(0)
    print("w+ content:", f.read())

with open("demo.txt", "a+") as f:
    f.write("Appended using a+\n")
    f.seek(0)
    print("a+ content:", f.read())
