import numpy as np

#vector
v = np.array([5, 2])

#matrix
matrix = np.array([[1, 2], 
                   [3, 4]])

#dot product (vector magic) - used in neural networks to compute activations
#Imagine you're scoring a test. You multiply scores by weights and add
v1 = np.array([3, 4]) # test scores
v2 = np.array([0.4, 0.6]) # weights
dot = np.dot(v1, v2) # 3x0.4 + 4x0.6 = 3.6
print(dot)