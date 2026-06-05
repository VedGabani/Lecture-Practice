from abc import ABC, abstractmethod

# 1. Define the Abstract Base Class
class BankAccount(ABC):
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# 2. Implement the Child Class
class Account(BankAccount):
    
    def __init__(self, balance, withdraw_limit, deposit_limit):
        self.balance = balance
        self.withdraw_limit = withdraw_limit
        self.deposit_limit = deposit_limit

    # Implementing the abstract withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw success! Remaining balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    # Implementing the abstract deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit success! New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

# --- Testing the Object-Oriented Code ---

# Create an account instance with initial values (balance, withdraw limit, deposit limit)
d = Account(10000, 2000, 5000)

# Interact with the object using dot (.) syntax
d.deposit(1000)
d.withdraw(100)
