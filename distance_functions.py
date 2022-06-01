import math
import scipy

def euclidean_distance(points):
    """
    Calculates the Euclidean distance between two points.

    Parameters
    ----------
    points : list
        A list of two points of equal dimension.

    Returns
    -------
    sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2)
    sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2)
    """
    distance = 0
    for i in range(len(points[0])):
        distance += (points[0][i] - points[1][i])**2


    return distance**(1/2)

def manhattan_distance(points):
    distance = 0
    for i in range(len(points[0])):
        distance += abs(points[0][i] - points[1][i])

    return distance

def maximum_distance(points):
    distance = 0
    list = []
    for i in range(len(points[0])):
        list.append(abs(points[0][i] - points[1][i]))

    return max(list)

def weighted_euclidean(weights, points):
    distance = 0
    for i in range(len(points[0])):
        distance += weights[0]*(abs(points[0][i] - points[1][i]))**2

    return distance**(1/2)

##def quadratic_form(points):



# print("Euclidean: " + str(euclidean_distance([[1,2,3], [3,4,5]])))
# print("Manhattan: " + str(manhattan_distance([[1,2,3], [3,4,5]])))
# print("Maximum: " + str(maximum_distance([[1,2,3], [3,4,5]])))
# print("Weighted Euclidean: " + str(weighted_euclidean([1,2], [[1,2,3], [3,4,5]])))
# ##print("Quadratic Form: " + str(quadratic_form([[1,2,3], [3,4,5]])))


