import pandas as pd

students = pd.DataFrame(
    {
        "name": ["Ada", "Bob", "Charly", "Dora", "Eve"],
        "group": ["A", "A", "B", "B", "A"],
        "points": [18, 12, 15, 9, 20],
        "submitted_project": [True, True, False, True, True],
    }
)

students["passed_exam"] = students["points"] >= 10
students["passed_course"] = students["passed_exam"] & students["submitted_project"]

summary = (
    students.groupby("group")
    .agg(avg_points=("points", "mean"), pass_count=("passed_course", "sum"))
    .reset_index()
)

print("Students:", students)
print("Group summary:", summary)
print("Top scorer:")
print(students.sort_values("points", ascending=False).head(1))
