from abc import ABC , abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def withdraw(self , ammount):
        pass

    @abstractmethod
    def deposit(self , amount):
        pass

class Account(BankAccount):

    def  __init__(self , balance, withdraw , deposit):
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit

#    def balance(self , amount):
 #       pass

    def withdraw(self , amount):
        if amount > 0:
            self.balance -= amount
            print("Withdraw")

        else:
            print("Invalid")

    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
            print("Done")

        else:
            print("Invalid")

#b = balance(10000)
d = Account(100000 , 10000 , 2000)
#w = Account()

d.deposit(1000) 
d.withdraw(100)
