#Bank 
class Bank:  
    def __init__(self, name, account_number, initial_balance=0):  
        self.name = name  
        self.account_number = account_number  
        self.initial_balance = initial_balance 
 
    def deposit(self, amount):  
        if amount > 0:
            self.initial_balance += amount  
            print("amount deposited successfully")  
        else:  
            print("amount not deposited")  
 
    def withdraw(self, amount):  
        if amount <= self.initial_balance:   
            print("Your amount withdrawn successfully")  
            self.initial_balance -= amount  
        else:  
            print("No sufficient funds in your account")  
 
    def check_balance(self):  
        print(f"Your remaining balance in the account is {self.initial_balance}")  
print("Holder1")
holder1 = Bank("Jin", 401219921306, 50000)  
holder1.deposit(7000)  
holder1.withdraw(2000)  
holder1.check_balance()  
print( "Holder2") 
holder2 = Bank("JHope", 180219941306, 25000)  
holder2.deposit(3000)  
holder2.withdraw(2000)  
holder2.check_balance() 
#cosmetics 
class Cosmetics: 
    def __init__(self, name="default",brand="default",price="default",category="default"): 
        self.name = name 
        self.brand = brand 
        self.price = price 
        self.category = category 
    def display(self): 
        print(f"Cosmetic Product Information:") 
        print(f"Name: {self.name}") 
        print(f"Brand: {self.brand}") 
        print(f"Price: {self.price} ") 
        print(f"Category: {self.category}") 
 
 
product1 = Cosmetics()  # Using default values
product1.display() 
 
product2 = Cosmetics(name="Lipstick", brand="L'Oréal", price=250, category="Makeup")   
product2.display()
