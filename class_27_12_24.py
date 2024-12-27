#Duck walking
class CreditCard:
    def pay(self,amount):
        return f"{amount} paid using Credit Card"
class PayPal:
    def pay(self,amount):
        return f"{amount} paid using Paypal"
class DebitCard:
    def pay(self,amount):
        return f"{amount} paid using Debit Card"

def process(cl,amount):
    print(cl.pay(amount))
cc=CreditCard()
process(cc,200)
pp=PayPal()
process(pp,300)
db=DebitCard()
process(db,400)