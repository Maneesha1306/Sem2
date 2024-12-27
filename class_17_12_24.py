class Library:
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"

class DigiLibrary(Library):
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"
    
Lib=Library()
dig=DigiLibrary()
book1=input()
user1= input()
book2=input()
user2=input()
print(Lib.issue_book(book1,user1))
print(dig.issue_book(book2,user2))