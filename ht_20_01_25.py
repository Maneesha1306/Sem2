class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def add_interest(self, rate):
        if rate > 0:
            interest = self.__balance * (rate / 100)
            self.__balance += interest
            print(f"Interest added: ${interest:.2f}")
        else:
            print("Invalid interest rate.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage
account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(200)
account.add_interest(5)
print(f"Account Number: {account.get_account_number()}")
print(f"Balance: ${account.get_balance():.2f}")
