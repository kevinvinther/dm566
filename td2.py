def td2(clusters):
    """
    Input:
        cluster: A cluster (a list of points)
    Output:
        total distance ^ 2
    """
     # initialize
    total_distance = 0
    for cluster in clusters:
        dist = 0
        mid = sum(cluster)/len(cluster)
        for p in cluster:
            dist = dist + abs(mid - p)
        total_distance +=  dist**2
    return total_distance

print(td2([[1,3], [3,4], [5,6]]))
