# Klasse + __str__

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


s = Student("Ada", 21)
print(s)


"""
Next:

* Create a class Price, which takes a floating point number and a currency as properties
* Override the +(add) operator for the class Price, to produce a new Price on adding two prices; throw an appropriate error when the currencies differ
"""