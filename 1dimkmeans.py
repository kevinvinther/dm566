import kmeans1d

x = [2, 6]
k = 2

clusters, centroids = kmeans1d.cluster(x, k);
print(clusters)
print(centroids)

x = [2, 4, 6]
k = 3

clusters, centroids = kmeans1d.cluster(x, k);
print(clusters)
print(centroids)


x = [2, 4, 6, 10]
k = 4

clusters, centroids = kmeans1d.cluster(x, k);
print(clusters)
print(centroids)

