from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class BankAccount(Account):

    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited -_- {amount}")

        else:
            print("Invalid amount")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn -_- {amount}")

        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

d = BankAccount("A101")

d.deposit(1000)
d.withdraw(10)

print("Balance:", d.get_balance())
