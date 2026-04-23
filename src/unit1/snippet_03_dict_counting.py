
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

students = dict()

class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

s1 = A('dave')
s2 = A('dave')
s3 = A('paul')

students[s1] = 'a'
students[s2] = 'b'
students[s3] = 'c'

print(students)

"""
Next:

* Create a new dict with three key-values pairs and "spread" the first dict's key-value pairs into it 
* Use the instances of the class Student as Key. What happens when use two Student instances with 
  the same name and age as keys? Which options do you have that they are considered to be the same key?
"""