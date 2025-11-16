import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [-50, 52, 100, 42, 31, 110, 12 , 8, 27, -10, 76, 111, 12, 63, -35, 30, 15, 47]
y = [120, 5, 27, 96, 121, -60, -47, 22, 0, -75, 5, 15, -12, 77, -38, 57, -96, -30]

data = list(zip(x, y))

kmeans = KMeans(n_clusters = 4)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()
