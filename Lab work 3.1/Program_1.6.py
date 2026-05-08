# Q-6

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined sentence:", sentence)

multiline_text = """Hello World
Python Programming
AI and Data Science"""

lines = multiline_text.splitlines()

print("\nLines:")
for line in lines:
    print(line)

text = "Hello Amazing World"

print("\nStarts with 'Hello':", text.startswith("Hello"))
print("Ends with 'World':", text.endswith("World"))

data_text = "Data123#Science!"
clean_text = ""

for char in data_text:
    if char.isalpha():
        clean_text += char

print("\nCleaned text:", clean_text)

word = "Python"
reversed_word = word[::-1]

print("Reversed string:", reversed_word)
