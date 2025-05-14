# distribution - tells us how data is spread
# normal distribution (bell curve)

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000) # mean 0, std dev 1
plt.hist(data, bins=30)
plt.title("Normal Distribution")
plt.show()

# Bayes' Theorem - helps us update belief after seeing evidence
# allowing one to find the probability of a cause given its effect
# ex: if someone sneezes, how likely are they sick?
# Formula: P(A|B) = ((P(B|A) ⋅ P(A)) ÷ (P(B)))

'''
    🧤 What's a Derivative?
    - It tells you how fast something is changing.
    - Imagine riding a bike — the speed is the derivative of your position.
    - In ML, we use derivatives to update our models and make them better.

    Gradients
    - A gradient is like a map that tells your AI model which way to move to make predictions better.

    Example:
    - If loss = 50 and we move a little and loss becomes 40 → that's a good direction.
    - We use the gradient to keep going in the best direction.
    - We'll use this in gradient descent next.
'''

