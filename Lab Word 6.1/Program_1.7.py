# Q-7

with open("sample.txt", "r") as f:
    content = f.read()

words = len(content.split())
characters = len(content)
lines = content.count("\n") + 1

print("Words:", words)
print("Characters:", characters)
print("Lines:", lines)
