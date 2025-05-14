import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

import pandas as pd
data = {"Name": ["A", "B"], "Score": [85, 90]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 1]
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()