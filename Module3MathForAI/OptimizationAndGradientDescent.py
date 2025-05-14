'''
    What's Optimization?
    - It's about finding the best model by minimizing a loss function (aka how wrong the model is).

    Gradient Descent
    - This is how models learn:
    - Guess a model (start anywhere)
    - Measure error (loss)
    - Follow the slope (gradient)
    - Repeat until it's low
'''

#simple gradient descent to minimize y=x^2
x = 10.0
learning_rate = 0.1
for i in range(20):
    gradient = 2 * x
    x = x - learning_rate * gradient
    print(f"step {i+1}: x = {x}")