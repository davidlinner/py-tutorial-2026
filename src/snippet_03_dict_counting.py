
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

"""
Next:

* Create a new dict with three key-values pairs and "spread" the first dict's key-value pairs into it 
* Use the instances of the class Student as Key. What happens when use two Student instances with 
  the same name and age as keys? Which options do you have that they are considered to be the same key?
"""