import random

while True:
    print("\n==== MENU ====")
    print("1. Hello Program")
    print("2. Add Two Numbers")
    print("3. Simple Calculator")
    print("4. Sandwich Maker")
    print("5. Pet Simulator")
    print("6. Rock Paper Scissors")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello world")
        name = input("Enter your Name: ")
        print("I am", name)

    elif choice == "2":
        a = 5
        b = 10
        print("The sum is:", a + b)

    elif choice == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Division:", a / b)
        print("Multiplication:", a * b)

    elif choice == "4":
        bread = input("Choose bread (White/Brown): ")
        filling = input("Choose filling (Cheese/Jelly): ")

        print("Here is your sandwich:")
        print(bread + " bread + " + filling + " + Hot sauce")

    elif choice == "5":
        pet = input("Select your Pet (Dog/Cat/Fish): ")

        if pet == "Dog":
            print("Here is your Dog woof!")
        elif pet == "Cat":
            print("Here is your Cat meow!")
        elif pet == "Fish":
            print("Here is your Fish Blob")
        else:
            print("We don't have that pet")

    elif choice == "6":
        choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choices)
        player = input("Choose Rock, Paper, Scissors: ")

        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie")
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            print("You win!")
        else:
            print("You lose!")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
