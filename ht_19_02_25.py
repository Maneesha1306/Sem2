#1
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

payment_methods = [CreditCard(), PayPal(), UPI()]
amount = 500
for method in payment_methods:
    method.pay(amount)
#2
def find_first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
numbers = [3, 1, 4, 2, 5, 3, 2]
print(find_first_duplicate(numbers))
