
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


s = Student("Ada", 21)
print(s)


class Price:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Price):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Cannot add prices with different currencies: {self.currency} and {other.currency}")
        return Price(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"


p1 = Price(10.50, "EUR")
p2 = Price(20.25, "EUR")
print(f"Total: {p1 + p2}")

try:
    p3 = Price(5.00, "USD")
    print(p1 + p3)
except ValueError as e:
    print(f"Error: {e}")



"""
Complete:
* Created a class Price with amount and currency
* Overrode the + operator with currency check
"""