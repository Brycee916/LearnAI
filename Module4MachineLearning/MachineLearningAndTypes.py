'''
    Machine Learning is giving a computer the ability to learn from data without being explicitly programmed for every rule.
    - Simple Example: You feed a machine photos of cats and dogs with labels. 
        It starts learning what makes a “cat” vs. a “dog” and can classify new photos it's never seen before.
    - Instead of writing rules like:
        if email.contains("free money"):
            label = "spam"
    - We let the machine learn from data:
        email_data = [email1, email2, ..., emailN]
        labels = [spam, not_spam, spam, ...]
        model.fit(email_data, labels)


    Basic Workflow:
    - Collect data
    - Preprocess data
    - Choose an algorithm
    - Train the model
    - Evaluate the model
    - Use the model to predict

    Types of Machine Learning
    1. Supervised Learning (Most common)
        - uses labeled data x and y
        - You give input and the correct output
        - Examples: Email spam detection, predicting house prices
        - Algorithms: Linear Regression, Decision Trees, k-NN, Logistic Regression
    2. Unsupervised Learning
        - You only give inputs, no labels
        - Model finds patterns
        - Examples: Customer segmentation, topic clustering, grouping students based on study habits
        - Algorithms: K-Means, PCA, Hierarchical Clustering
    3. Reinforcement Learning
        - An agent learns to act in an environment by receiving rewrads or penalties
        - Learns via rewards
        - Example: Game-playing AI (chess, Atari)
        - Algorithms: Q-Learning, DQN
'''
# Supervised ML with labeled data
# Predicting a house price (input = features, output = price)
X = [[3], [4], [5]]  # Bedrooms
y = [150000, 200000, 250000]  # Price

# Unsupervised learning, k-means finds natural groupings in unlabeled data
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(x)
#
# You give the data, model groups it
data = [[25, 40000], [40, 80000], [22, 25000]]  # age + income
