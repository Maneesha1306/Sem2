class Price_handling:
    def __init__(self,base_price,tax,discount):
        self.base_price= base_price
        self.tax=tax
        self.discount=discount

    def calculate_final_price(self):
        try:
            if self.base_price<0 or self.discount<0 or self.tax<0:
                raise ValueError("Values cannot be negative")
            else:
                total=self.base_price+((self.tax/100)*self.base_price)-((self.discount/100)*self.base_price)
                return total
        except ValueError as e:
            print(e)

b=int(input("Base Price:"))
t=int(input("Tax Percentage:"))
d=int(input("Discount Percentage:"))
p=Price_handling(b,t,d)
p.calculate_final_price()