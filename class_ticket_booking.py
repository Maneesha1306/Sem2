import random

class Customer:
    def __init__(self, cust_id, name, phone):
        self.cust_id = cust_id
        self.name = name
        self.phone = phone

    def gen_rand_id(self):
        c_id = random.randint(1000, 9999)
        return f"TICK{c_id}"

    @staticmethod
    def verify_customer_id(cust_id):
        if cust_id[0:4] == "TICK" and cust_id[4:8].isdigit():
            return True
        else:
            return False


class TicketBooking:
    def __init__(self):
        self.events = {
            "Concert": {"price": 500, "seats": 100},
            "Movie": {"price": 150, "seats": 200},
            "Drama": {"price": 100, "seats": 250},
            "Match": {"price": 1500, "seats": 1000}
        }
        self.booked_tickets = []

    def view_events(self):
        for event, details in self.events.items():
            print(f"{event}: {details['price']} per ticket, {details['seats']} seats available")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event["seats"] >= quantity:
                total_price = event["price"] * quantity
                event["seats"] -= quantity
                self.booked_tickets.append({
                    "customer_id": customer.cust_id,
                    "event": event_name,
                    "quantity": quantity,
                    "total_price": total_price,
                })
                print(f"Tickets booked for {event_name} - Total Price: {total_price}")
            else:
                print("Seats not available!")
        else:
            print("Event name is not available!")

    def view_tickets(self, customer):
        print("Ticket Information")
        cus_ticket = [t for t in self.booked_tickets if t["customer_id"] == customer.cust_id]
        if not cus_ticket:
            print("No tickets booked.")
        else:
            for tick in cus_ticket:
                print(f"Event: {tick['event']}, Quantity: {tick['quantity']}, Total cost: {tick['total_price']}")


# Main Program
book = TicketBooking()
print("Welcome To Ticket Booking Program")

cust_id = input("Enter the Customer Id: ")
if Customer.verify_customer_id(cust_id):
    name = input("Enter the name: ")
    phone = int(input("Enter the phone: "))
    customer = Customer(cust_id, name, phone)
    print("*** Booking details ****")
else:
    print("Invalid!!! Please Register")
    name = input("Enter the name: ")
    phone = int(input("Enter the phone: "))
    cust_id = Customer.gen_rand_id(Customer)
    customer = Customer(cust_id, name, phone)
    print("Your Customer Id is ", cust_id)

while True:
    print("\nBooking Info*")
    print("\n1. View Events")
    print("\n2. Book Tickets")
    print("\n3. View Tickets")
    print("\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        book.view_events()
    elif choice == "2":
        event_name = input("Enter the name of any event: ")
        quantity = int(input("Enter the number of tickets: "))
        book.book_tickets(event_name, quantity, customer)
    elif choice == "3":
        book.view_tickets(customer)
    elif choice == "4":
        print("Successfully Your Tickets are Booked")
        quit()
    else:
        print("Invalid choice! Please try again.")