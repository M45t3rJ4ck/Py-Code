import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

centers = [[1, 1], [5, 5]]
X, Y = make_blobs(n_samples=10000, centers=centers, cluster_std=1)
plt.scatter(X[:, 0], X[:, 1])
plt.show()
MeanShift.fit(X)
labels = MeanShift.labels_
cluster_centers = MeanShift.cluster_centers_
n_clusters_ = (len(np.unique(labels)))
colors = 10*["r.", "b.", "g.", "c.", "m.", "k.", "y."]
for i in range(len(x)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)
plt.scatter(cluster_centers[:,0], cluster_centers[:.1], marker=X, s=150, linewidths=5, zorder=10)
plt.show()
