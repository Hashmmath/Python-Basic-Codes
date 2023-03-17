'''The KNN class is initialized with the number of neighbors to consider, k. The fit method takes in a training dataset X and its corresponding labels y and stores them as instance variables. The predict method takes in a test dataset X and returns an array of predicted labels. The _predict method predicts the label for a single data point.

For each test data point x, _predict computes the Euclidean distance to each training data point x_train, stores the indices of the k closest neighbors, and retrieves their corresponding labels. It then returns the label that occurs most frequently among the k nearest neighbors.

Note that this implementation assumes that the input features and labels are in numpy arrays.'''


import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        distances = [np.sqrt(np.sum((x - x_train)**2)) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
