

def kmeans(points, initial_means):
    num_clusters = len(initial_means)
    
    for i in points:
        distance1 = abs(i - initial_means[0])
        distance2 = abs(i - initial_means[1])
        print("Distance from point " + str(i) + " to cluster " + str(initial_means[0]) + " is " + str(distance1))
        print("Distance from point " + str(i) + " to cluster " + str(initial_means[1]) + " is " + str(distance2))

kmeans([2,3,4,10,11,12,20,25,30], [2,6])