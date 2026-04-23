# Set + Duplikate entfernen + Mengenoperationen

course_a = {"Ada", "Bob", "Charly"}
course_b = {"Bob", "Dora", "Ada"}

both = course_a & course_b
all_students = course_a | course_b
only_a = course_a - course_b

print(both)
print(all_students)
print(only_a)

"""
Next: 

* Ass a check if course_a contains Charly
"""