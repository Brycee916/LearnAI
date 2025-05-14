#predict a continuous like price of cookies
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

#example dataset
x = np.array([[i] for i in range(1, 21)])  # 20 samples
y = np.array([i * 1.25 for i in range(1, 21)])  # perfect linear relationship, each cookie costs 1.25

#split data 80/20, 80% for training, 20% for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#train the model
model = LinearRegression()
model.fit(x_train, y_train) #80% training data to create the model

#predict
predictions = model.predict(x_test)

#evaluate
print("Predictions:", predictions)
print("Actual:", y_test)
print("R2:", model.score(x_test, y_test))
print("R² Score:", r2_score(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))

#plot using plt
plt.scatter(x, y, color="blue", label="all data")
plt.scatter(x_test, y_test, color="red", label="test data")
plt.plot(x, model.predict(x), color="green", label="Regression line (cookie prices)")
plt.title("Linear Regression: number of cookies vs price")
plt.xlabel("cookies")
plt.ylabel("price")
plt.legend()
plt.grid(True)
plt.show()

#predict a y-value for custom x
custom_x = np.array([[25]])
predicted_y = model.predict(custom_x)
print(f"Price for 25 cookies: y = {predicted_y[0]:.2f}")

#predict another y-value for custom x
custom_x2 = np.array([[100]])
predicted_y2 = model.predict(custom_x2)
print(f"Price for 100 cookies: y = {predicted_y2[0]:.2f}")