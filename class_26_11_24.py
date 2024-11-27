class Books:
    def __init__(self,b_name,b_author,b_price):
        self.b_name=b_name
        self.b_author=b_author
        self.b_price=b_price
    def show(self):
        print('Books:',self.b_name,self.b_author,self.b_price)
book1=Books("Harry Potter","J.K.Rowling",500)
book1.show()
book2=Books("Ramayana","Kalki",800)
book2.show()

class Books:
    def __init__(self):
        self.bname="Pride and prejudice"
        self.bauthor="Jane"
    def display(self):
        print(f"Book name={self.bname}\nBook author={self.bauthor}")
lib=Books()
lib.display()

class Books:
    library_name = 'ABC Publishers'
    def __init__(self,name,publishing =893):
        self.name = name#instance variables
        self.publishing=publishing
    def show(self):
        print(self.name,self.publishing)
book1=Books("Ram c/o anandhi")
book1.show()
