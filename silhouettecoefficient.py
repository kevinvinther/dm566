import math

def calculate_cluster_mean(points):
    """
    Input:
        cluster: A cluster (a list of points)
    Output:
        The mean of the points in the cluster.
    """
    x = 0
    y = 0
    for point in points:
        x += point[0]
        y += point[1]
    x = x / len(points)
    y = y / len(points)
    return (x, y)

def get_average_point(cluster, point_list):
    """
    Input:
        cluster: A cluster (a list of points)
        point_list: List of points
    Output:
        The mean of the points in the cluster.
    """
    count = 0
    new_points = []
    for point in point_list:
        new_points.append(round(math.sqrt(abs(point[0] - cluster[0])**2 + abs(point[1] - cluster[1])**2), 3))

    return new_points

print(get_average_point((4,3.25), [(10,1), (2,3), (3,4), (1,5)]))

def silhouette_coefficient(cluster_list, point_list):
    """
    Input:
        cluster_list: List of clusters where each cluster is a list of points (as before)
        point_list: List of points
    Output:
        The silhouette score of the clustering
    """
    silhouette_coefficient = 0
    calculated_clusters = []
    for cluster in cluster_list:
        calculated_clusters.append(get_average_point(cluster, point_list))

    for point in point_list:
        min_distance = 100
        for cluster in calculated_clusters:
            distance = math.sqrt(abs(point[0] - cluster[0])**2 + abs(point[1] - cluster[1])**2)
            if distance < min_distance:
                min_distance = distance
        silhouette_coefficient += (min_distance - abs(point[0] - calculated_clusters[0][0])) / min_distance

    return silhouette_coefficient / len(point_list)
