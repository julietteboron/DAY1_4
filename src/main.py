from scripts.BasicStats import moyenne
from sklearn.datasets import make_blobs

data = make_blobs(n_samples=100, centers=6, n_features=4, random_state=42)
print(moyenne(data))