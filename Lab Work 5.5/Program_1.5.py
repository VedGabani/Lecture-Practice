from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Account):
    
# __ it mean private

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

    def _set_balance(self, new_balance):
        self.__balance = new_balance

class SavingAccount(BankAccount):

    def __init__(self , account_number , balance , interest):
        BankAccount.__init__(self , account_number , balance)
        self.interest_rate = interest

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added -_- ", interest)

class CurrentAccount(BankAccount):

    def __init__(self , account_number , balance , overdraft = 10000):

        BankAccount.__init__(self , account_number , balance)
        self.overdraft = overdraft

    def withdraw(self , amount):

        if amount <= self.get_balance() + self.overdraft:
            new_bal = self.get_balance() - amount
            self._set_balance(new_bal)
            print("Withdraw -_- ", amount)

        else:
            print("Limit overdraft")


d = BankAccount("A101")
d.deposit(1000)
d.withdraw(10)
print("Balance -_- ", d.get_balance())

print("\n--- Saving Account ---\n")
s = SavingAccount("B101", 100000, 5)
s.add_interest() 
s.deposit(2000)
s.withdraw(1000)
print("Saving Balance -_- ", s.get_balance())

print("\n--- Current Account ---\n")
c = CurrentAccount("C101", 100000, 10)
c.withdraw(1000)
print("Current Balance -_- ", c.get_balance())
