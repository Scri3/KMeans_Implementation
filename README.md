## KMeans Algorithm on 2D data points

Implementation of **K-Means clustering** algorithm on a set of 2D points and
visualization of the clustered data using a scatter plot.\
 To use this script for your own data points:

1.  Replace your values with `x` and `y`.
2.  The given data points will be paired as coordinates.
3.  In this script, the number of clusters is **four**, meaning the algorithm will divide the data into four clusters. Replace your effective centroid value `'n'` in `KMeans(n_clusters = n)`
4.  **KMeans** from `scikit-learn` iteratively assigns each data point to the nearest centroid until the data points are  grouped into
    stabilized clusters.
5.  Data points will be plotted with `matplotlib` and color‑coded by their assigned
    cluster. Finally, `plt.show()` displays the scatter plot window.

