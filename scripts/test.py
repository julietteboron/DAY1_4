import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]])
plt.imshow(A, cmap='gray')
plt.show()

import pandas
from sklearn.datasets import make_blobs

data = make_blobs(n_samples=100, centers=6, n_features=2, random_state=42)
plt.scatter(data[0][:, 0], data[0][:, 1], c=data[1])
plt.show()












