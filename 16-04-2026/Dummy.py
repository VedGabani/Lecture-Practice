# Pythn basic fundamental statements

print("Hello world")
name = input("Enter your Name -_- ")
print("I am ", name)

# How to add two numbers

a = 5
b = 10

sum = a+b
print("The sum is -_- ", sum)

# Simple calculator

a = int(input("Enter the First number -_- "))
b = int(input("Enter the Second number -_- "))

print("Addition is -_- ", a+b)
print("Subtraction is -_- ", a-b)
print("Division is -_- ", a/b)
print("Multiplicaton is -_- ", a*b)

# Silly sandwich maker

bread = input("Choose your Bread (White/Brown) -_- ")
filling = input("Choose your filling (Cheese/Jelly) -_- ")

print("Here is your Silly sandwhich")
print("["+bread + " bread + " + filling + " + Hot sause ]")

# Pet simulator

pet = input("Select your Pet (Dog/Cat/Fish) -_- ")

if pet == "Dog":
    print("Here is your Dog wof!")

elif pet == "Cat":
    print("Here is your Cat meow!")

elif pet == "Fish":
    print("Here is your Fish Blob")

else:
    print("We don't have that Pet Sorry!")

# Rock,Paper and Scissors

import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)
player = input("Choose Rock,Paper and Scissors -_- ")

if player == computer:
    print("It's Tie.......")

elif (player == "Rock" and computer == "Scissors") or\
      (player == "Paper" and computer == "Rock") or\
      (player == "Scissors" and computer == "Paper"):
    print("You wins!!!!!")

else:
    print("Computer Wins")
