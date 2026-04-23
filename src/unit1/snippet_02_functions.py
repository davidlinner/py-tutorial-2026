
def greet(name, greeting="Hello", excited=False):
    text = f"{greeting}, {name}"
    if excited:
        text += "!"
    return text

print(greet("Ada", excited=True))
print(greet("Bob", greeting="Hi", excited=True))


"""
Next:

* Find out how function scopes work in Python, define a global variable and mutate it in your function
* How to pass more named parameters to a Python function without defining them
* Return a tuple from a function
"""