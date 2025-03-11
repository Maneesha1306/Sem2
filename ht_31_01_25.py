import re
class Theatre:
    def __init__(self, name, phno, dob, noofseats):
        self.name = name
        self.phno = phno
        self.dob = dob
        self.noofseats = noofseats
        self.seats = []
        self.snacks_ordered = {}
        self.gst = 0.18
        self.snack_prices = {"Popcorn": 100, "Ice Cream": 80, "Puffs": 60,"Tea": 40, "Soft Drinks": 50}
    def select_seats(self):
        print("Available Seats:")
        print("First Class (A-G) - Rs.200 + GST")
        print("Second Class (G-X) - Rs.150 + GST")
        print("Economic Class (Y-Z) - Rs.50 + GST")
        for _ in range(self.noofseats):
            seat = input("Select Your Seat (e.g., A2): ")
            if re.match(r"^[A-Z][0-9]+$", seat):
                self.seats.append(seat)
            else:
                print("Invalid seat format. Try again.")
    def calculate_ticket_price(self):
        first_class_rows = "ABCDEFG"
        second_class_rows = "GHIJKLMNOPQRSTUVWX"
        economic_class_rows = "YZ"
        price = 0
        for seat in self.seats:
            row = seat[0].upper()
            if row in first_class_rows:
                price += 200 + (200 * self.gst)
            elif row in second_class_rows:
                price += 150 + (150 * self.gst)
            elif row in economic_class_rows:
                price += 50 + (50 * self.gst)
        return round(price, 2)
    def select_snacks(self):
        snack_choice = input("Do you want Snacks? (Yes/No): ").strip().lower()
        if snack_choice == "yes":
            print("1. Popcorn - Rs.100\n2. Ice Cream - Rs.80\n3. Puffs -Rs.60\n4. Tea - Rs.40\n5. Soft Drinks - Rs.50")
        no_of_snacks = int(input("No of Snacks: "))
        for _ in range(no_of_snacks):
            snack = input("Enter snack name: ").strip()
            qty = int(input("Enter quantity: "))
        self.snacks_ordered[snack] = self.snacks_ordered.get(snack, 0)+ qty
    def calculate_snack_price(self):
        return sum(self.snack_prices.get(snack, 0) * quantity for snack,quantity in self.snacks_ordered.items())
    def display_summary(self):
        total_ticket_price = self.calculate_ticket_price()
        total_snack_price = self.calculate_snack_price()
        print(f"\nHi {self.name}..! You have successfully booked{len(self.seats)} tickets. Seats: {', '.join(self.seats)}")
        print(f"Your total ticket price: Rs.{total_ticket_price}")
        if total_snack_price:
            print(f"Your snacks price: Rs.{total_snack_price}")
            print(f"Total payable amount: Rs.{total_ticket_price +total_snack_price}")

name = input("Enter your name: ")
phno = input("Enter Your Phone Number: ")
dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
noofseats = int(input("Select total number of seats: "))
booking = Theatre(name, phno, dob, noofseats)
booking.select_seats()
booking.select_snacks()
booking.display_summary()
