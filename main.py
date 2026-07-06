from scripts.BasicStats import datalen, moyenne
from sklearn.datasets import make_blobs

X, Y = make_blobs(n_samples=100, n_features=4, random_state=42)
print(moyenne(X))