
class Calculator:
    def __init__(self, val1, val2):
        if not isinstance(val1, int) or not isinstance(val2, int):
            raise ValueError("Both values must be integers.")
        self.val1 = val1
        self.val2 = val2
    def calculate(self):
        while True:
            try:
                print("Enter your choice (+, -, *, /, Q to Quit): ")
                CH = input("Enter your choice: ").strip()
                if CH not in ['+', '-', '*', '/', 'Q']:
                    raise KeyError("Invalid operation.")
                if CH == '+':
                    return f"Result: {self.val1 + self.val2}"
                elif CH == '-':
                    return f"Result: {self.val1 - self.val2}"
                elif CH == '*':
                    return f"Result: {self.val1 * self.val2}"
                elif CH == '/':
                    if self.val2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    return f"Result: {self.val1 / self.val2}"
                elif CH == 'Q':
                    print("Exiting the program.")
 
            except KeyError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)
while True:
    try:
        Val1 = int(input("Enter value 1: "))
        Val2 = int(input("Enter value 2: "))
        print(f"The Value1 is: {Val1}")
        print(f"The Value2 is: {Val2}")
        check = Calculator(Val1, Val2)
        result = check.calculate()
        if result:
            print(result)
            break
    except ValueError:
        print("Provided non-numeric input. Please retry.")