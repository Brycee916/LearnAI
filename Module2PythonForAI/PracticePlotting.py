#Practice
import pandas as pd
import matplotlib.pyplot as plt
print("\n\n----------------------------------------------")
print("Practice Assignment")
test_scores = {"Student": ["John", "Terry", "Samantha"], "Score": [75, 93, 88]}
df = pd.DataFrame(test_scores)
print(df)
x = df['Student']
y = df['Score']
plt.plot(x, y, marker='o', color='black')
plt.title("Test Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.grid()
plt.show()