import random

names = ["Ada", "Bob", "", "Charly"]

upper_names = []
for name in names:
    if name:
        upper_names.append(name.upper())

for i in range(0, 10):
    print(i)

print(upper_names)

# Create a list with 20 random numbers and obtain a range
random_numbers = [random.randint(1, 100) for _ in range(20)]
print(f"Random numbers: {random_numbers}")

range_10_to_15 = random_numbers[10:-2]
print(f"Range from index 10 to 15 (exclusive): {range_10_to_15}")

"""
Next:
* Create a list with 20 random numbers and obtain a range from the list, e.g. 10 to 15 (exclusive) 
* Concatenate two lists
* Destructure (in Python called "unpack") the first two elements of the list 'names' 
  and the remaining elements into a list 'other'
* Replace the loop with list comprehension
"""