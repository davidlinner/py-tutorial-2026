# Generator + yield

def countdown(start):
    current = start
    while current > 0:
        yield current
        current -= 1

for number in countdown(5):
    print(number)


"""
Next:

* Recreate the Python range generator as 'span' generator
* Create a generator producing the fibonacci sequence
"""