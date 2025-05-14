#Logistic Regression: A simple classifier
#Logistic Regression is a machine learning algorithm used for classification problems.
#It predicts the probability of a data point belonging to a particular class.
#Despite the name "regression," it's used for classification — like "Is this flower Iris Setosa or not?"
#It models the **log-odds** of the target variable using a **sigmoid function** to squeeze output between 0 and 1.

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#load the iris dataset, it includes measurements of iris flowers and their species.
iris = load_iris()
x = iris.data #Features: sepal length, sepal width, petal length, petal width
y = iris.target #Labels: 0 = Setosa, 1 = Versicolor, 2 = Virginica

#split into training and test datasets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#train the model
model = LogisticRegression(max_iter=200) # max_iter ensures convergence

#fit (train) the model on the training data
model.fit(x_train, y_train)

#evaluate the accuracy on test data: how many samples did it correctly classify?
accuracy = model.score(x_test, y_test)
print("Model accuracy:", round(accuracy * 100, 2), "%")

#Predict the species of flower
sample_flower = [[5.1, 3.5, 1.4, 0.2]] # measurements of sample flower
prediction = model.predict(sample_flower)
predicted_class = iris.target_names[prediction[0]]
print("Predicted species of flower: ", predicted_class)

sample_flower2 = [[2.0, 5.5, 8.0, 1.2]]
prediction = model.predict(sample_flower2)
predicted_class = iris.target_names[prediction[0]]
print("Predicted species of flower: ", predicted_class)

# - Logistic regression doesn't give a continuous value like linear regression.
# - It uses the sigmoid (logistic) function to classify inputs.
# - It's good for binary or multiclass classification (like the iris dataset).

'''
    When we train the model, it tries over and over to get better at guessing the right answers. 
    max_iter=200 just means: “Hey model, you can try up to 200 times to get really good. 
    If you figure it out before that, great — but don't try forever.”
    When logistic regression trains, it uses a method like gradient descent (or similar solvers like 'lbfgs', 'saga', etc.) to minimize a loss function — this is called convergence.

    Convergence means the model has "settled" on the best parameters — the loss/error is not improving much anymore.
    If it doesn't converge, the model hasn't learned properly and your predictions may be bad.
'''