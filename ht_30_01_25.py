#1
import re
class UserInput:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.email = ""
        self.print_count = 0

    def validate_name(self, name):
        pattern = r'^(?=.*\d)(?=.*[!@#$%^&*()]).+$'
        return bool(re.match(pattern, name))

    def validate_password(self, password):
        pattern = r'^[a-zA-Z_#@]{1,8}$'
        return bool(re.match(pattern, password))

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def get_input(self):
        while True:
            self.name = input("Enter your Name: ")
            if not self.validate_name(self.name):
                print("Invalid Name. It must contain at least one number and one special character.")
                continue
            break

        while True:
            self.password = input("Enter your Password: ")
            if not self.validate_password(self.password):
                print("Invalid Password. It must not contain numbers and special characters except (#, _ and @) and should not be greater than 8 in length.")
                continue
            break

        while True:
            self.email = input("Enter your Email Address: ")
            if not self.validate_email(self.email):
                print("Invalid Email format.")
                continue
            break

        self.print_count = int(input("How many times to want to Print? "))

    def display(self):
        print(f"{self.name} wants to print {self.print_count} times and send mail to {self.email}.")
        print(f"Your password {self.password} will be encrypted and will be stored.")

user_input = UserInput()
user_input.get_input()
user_input.display()

#2
import re

class Banu:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.password = ""
        self.encoded_name = ""

    def validate_password(self, password):
        pattern = r'^(?=.*\d)(?=.*[!@#$%^&*()]).{1,8}$'
        return bool(re.match(pattern, password))

    def get_input(self):
        self.name = input("Enter your Name: ")
        self.department = input("Enter your Department: ")

        attempts = 0
        while attempts < 3:
            self.password = input("Enter your Password: ")
            re_password = input("Re-Type your Password: ")
            if self.password == re_password and self.validate_password(self.password):
                self.encoded_name = f"{self.name} - Fresher"
                break
            else:
                print("Passwords do not match or invalid format. Please try again.")
                attempts += 1

        if attempts == 3:
            print("Too many incorrect attempts. Please choose 'Forgot Password' to reset.")

    def display(self):
        print(f"Your Encoded Name is: {self.encoded_name}")
        print(f"Your Department is: {self.department}")
        print(f"Your Password is: {self.password}")


banu = Banu()
banu.get_input()
banu.display()