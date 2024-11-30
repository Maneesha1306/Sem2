#1
class Library:
    def __init__(self):
        self.books = {}  
    def add_book(self, book_name, quantity):        
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f'Book "{book_name}" added with quantity {quantity}.')
    def display_books(self):
        print("\nAvailable Books in Library:")
        for book, quantity in self.books.items():
            print(f' - {book}: {quantity} copies')

class Member:
    def __init__(self, member_name):
        self.member_name = member_name
        self.borrowed_books = []
    def borrow_book(self, book_name, library):
        if library.books.get(book_name, 0) > 0:
            library.books[book_name] -= 1
            self.borrowed_books.append(book_name)
            print(f'{self.member_name} borrowed "{book_name}".')
        else:
            print(f'Sorry, "{book_name}" is not available in the library.')
    def return_book(self, book_name, library):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            library.books[book_name] += 1
            print(f'{self.member_name} returned "{book_name}".')
        else:
            print(f'{self.member_name} does not have "{book_name}".')
    def display_borrowed_books(self):
        print(f'\nBooks borrowed by {self.member_name}:')
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f' - {book}')
        else:
            print("No books borrowed.")

class LibraryManagement:
    def __init__(self):
        self.library = Library()
    def add_member(self, member_name):
        return Member(member_name)
    def borrow_book(self, member, book_name):
        member.borrow_book(book_name, self.library)
    def return_book(self, member, book_name):
        member.return_book(book_name, self.library)

system = LibraryManagement()

system.library.add_book("To Kill a Mockingbird", 5)
system.library.add_book("Demian", 3)

system.library.display_books()

john = system.add_member("John Doe")

system.borrow_book(john, "Demian")
john.display_borrowed_books()
system.library.display_books()

system.return_book(john, "Demian")
john.display_borrowed_books()
system.library.display_books()

#2
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}
    def add_menu_item(self, item, price):
        self.menu[item] = price
    def display_menu(self):
        print(f"\nMenu at {self.name}:")
        for item, price in self.menu.items():
            print(f" - {item}: ${price:.2f}")
    def prepare_order(self, items):
        missing_items = [item for item in items if item not in self.menu]
        if missing_items:
            print(f"Cannot prepare: {', '.join(missing_items)} not on the menu.")
            return False
        print("Order prepared successfully!")
        return True

class Delivery:
    def assign_rider(self, order_id, rider):
        print(f"Order #{order_id} assigned to rider {rider}.")
    def track_order(self, order_id, rider):
        print(f"Order #{order_id} is being delivered by {rider}.")

class Order:
    def __init__(self, order_id, restaurant, delivery):
        self.order_id = order_id
        self.restaurant = restaurant
        self.delivery = delivery
        self.items = []
    def add_items(self, *items):
        self.items.extend(items)
    def process(self):
        if self.restaurant.prepare_order(self.items):
            self.delivery.assign_rider(self.order_id, "Rider John")


restaurant = Restaurant("Tasty Treats")
restaurant.add_menu_item("Burger", 5.99)
restaurant.add_menu_item("Pizza", 8.99)
restaurant.display_menu()

delivery = Delivery()
order = Order(101, restaurant, delivery)
order.add_items("Burger", "Pizza")
order.process()
delivery.track_order(101, "Rider John")
