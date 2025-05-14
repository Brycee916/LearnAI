import matplotlib.pyplot as plt
import pandas as pd

students = ["Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ian", "Jasmine",
    "Kevin", "Lily", "Michael", "Nina", "Oscar",
    "Paula", "Quentin", "Rachel", "Sam", "Tina"]
grades = [88, 92, 76, 85, 90,
    79, 84, 91, 73, 95,
    87, 89, 82, 77, 93,
    80, 86, 94, 78, 81]

students_grades = {"Student": students, "Grades": grades}
df = pd.DataFrame(students_grades)
print(df)

average_grade = df["Grades"].mean()
print("Average grade: ", average_grade)

plt.figure(figsize=(10,5))
plt.bar(df["Student"], df["Grades"], color="skyblue")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.title("Student Grades Vs. Average")
plt.axhline(y=average_grade, color="red", linestyle="--", linewidth=1.5, label=f"Average: {average_grade: .2f}")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid()
plt.show()