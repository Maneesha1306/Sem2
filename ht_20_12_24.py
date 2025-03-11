import random 
import re 
 
class Member: 
    def _init_(self, member_id, name, email): 
        self.member_id = member_id 
        self.name = name 
        self.email = email 
 
    def verify_email(self): 
        ex = r'^[a-z0-9._%+-]+@gmail\.com$' 
        if re.match(ex, self.email):  # use self.email 
            print("Valid email id") 
        else: 
            print("Email id is not valid") 
 
    def verify_member_id(self): 
        mem = r'^LIB\d{4}$' 
        if re.match(mem, self.member_id):  # use self.member_id 
            print("Valid member id") 
        else: 
            self.generate_member_id() 
 
    def generate_member_id(self): 
        self.member_id = "LIB" + str(random.randint(1000, 9999)) 
        print(f"Generated new member id: {self.member_id}") 
 
class Library(Member): 
    def _init_(self, member_id, name, email, book_id, title, author): 
        super()._init_(member_id, name, email)  # super() is better for inheritance 
        self.book_id = book_id 
        self.title = title 
        self.author = author 
    def display_overall(self): 
        print("Member id:", self.member_id) 
        print("Name:", self.name) 
        print("Email:", self.email) 
        print("Book borrowed or returned id:", self.book_id) 
        print("Book title:", self.title) 
        print("Author:", self.author) 
# Taking inputs from the user 
member_id = input("Enter the id of the member: ") 
name = input("Enter the name: ") 
email = input("Enter the email id: ") 
book_id = input("Enter the book id: ") 
title = input("Enter the book title: ") 
author = input("Enter the name of the author: ") 
a = Library(member_id, name, email, book_id, title, author) 
a.verify_email() 
a.verify_member_id() 
a.display_overall()