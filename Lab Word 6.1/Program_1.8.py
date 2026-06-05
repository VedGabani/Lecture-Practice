# Q-8

with open("sample.txt", "r+") as f:
    print("Existing content:")
    print(f.read())
    
    f.write("\nThis file was last modified by adding this sentence.")

print("Content updated.")
