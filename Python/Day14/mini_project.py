from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, holder_name, balance):
        self.__holder_name = holder_name
        self.__balance = balance

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Current Balance: {self.__balance}")
        else:
            print("Invalid Amount!")

    def _set_balance(self, balance):
        self.__balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            return
        balance = self.get_balance()

        if amount <= balance:
            self._set_balance(balance - amount)
            print("Withdraw Successful!")
            print(f"Current Balance: {self.get_balance()}")
        else:
            print("Insufficient Balance!")

    def __str__(self):
        return f"SavingsAccount({self.get_holder_name()}, Balance={self.get_balance()})"
    
    def __eq__(self, other):
        if self.get_balance() == other.get_balance():
            return "Balance is equal"
        else:
            return "Balance is not equal"


class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            return
        balance = self.get_balance()
        overdraf = balance + 1000

        if amount <= balance + 1000:
            self._set_balance(balance - amount)
            print("Withdraw Successful!")
            print(f"Current Balance: {self.get_balance()}")
        else:
            print("Insufficient Balance!")

    def __str__(self):
        return f"CurrentAccount({self.get_holder_name()}, Balance={self.get_balance()})"
    
    def __eq__(self, other):
        if self.get_balance() == other.get_balance():
            return "Balance is equal"
        else:
            return "Balance is not equal"


accounts = [
    SavingsAccount("Harpit", 5000),
    CurrentAccount("Luffy", 10000)
]

for account in accounts:
    account.withdraw(600)