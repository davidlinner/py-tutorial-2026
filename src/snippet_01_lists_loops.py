
names = ["Ada", "Bob", "", "Charly"]

upper_names = []
for name in names:
    if name:
        upper_names.append(name.upper())

print(upper_names)

"""
Next:
* Create a list with 20 random numbers and obtain a range from the list, e.g. 10 to 15 (exclusive) 
* Concatenate two lists
* Destructure (in Python called "unpack") the first two elements of the list 'names' 
  and the remaining elements into a list 'other'
* Replace the loop with list comprehension
"""