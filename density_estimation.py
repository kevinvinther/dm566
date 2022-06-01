import distance_functions

from collections import Counter

import itertools

def density_estimation(points):
    """
    Calculates the density of a set of points.
    :param points: list of points
    :return: density of the points
    """
    k = 0  # number of nearest neighbors (includes self), remember to +1
    n = 20 # number of points
    epsilon = 2 # radius of the neighborhood
    iterator = -1
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for point in points:
        iterator += 1
        distance_to_point = dict()
        # find the k nearest neighbors
        # we will only use this if we're not given epsilon
        if epsilon == 0:
            for point2 in points:
                distance_to_point["(" + str(point2[0]) + ", " + str(point2[1]) + ")"] = round(distance_functions.manhattan_distance([point, point2]), 2)

            # The value we're looking for
            value = (sorted(distance_to_point.items(), key=lambda x: x[1])[k -1 ])

            # The amount of values in the entire dictionary 
            value_amount = sum([1 for i in distance_to_point.values() if i == value[1]])
            #print(value[1])
            #print(value_amount)

            distance_to_point = sorted(distance_to_point.items(), key=lambda x: x[1])

            value_in_list = 0
            
            for i in distance_to_point[:k]:
                if i[1] == value[1]:
                    value_in_list += 1

            kp = k + (value_amount - value_in_list)
            #print(list(distance_to_point)[-1][1])
            # [1, 2, 3, 3, 3, 3] k = 4, value_amount = 4, amount_in_k = 2
            volume = 2 * list(distance_to_point[:k])[-1][1]**2
            #print(distance_to_point)
            #print("volume = " + str(volume))

            print(str(alphabet[iterator]) + ": " + str(kp) + '/(' + str(n) + ' * ' + str(volume) + ')\t = ' + str(kp / (n * volume)))
        
        if k == 0:
            def isLessThanOrEqualToEpsilon(x):
                return x <= epsilon
            
            for point2 in points:
                distance_to_point["(" + str(point2[0]) + ", " + str(point2[1]) + ")"] = round(distance_functions.manhattan_distance([point, point2]), 2)

            distance_to_point = sorted(distance_to_point.items(), key=lambda x: x[1])

            new_list = []
            for i in distance_to_point:
                if i[1] <= epsilon:
                    new_list.append(i[1])

            kp = len(new_list)

            volume = 2 * epsilon**2

            print(str(alphabet[iterator]) + ": " + str(kp) + '/(' + str(n) + ' * ' + str(volume) + ')\t = ' + str(kp / (n * volume)))



 
            
        
density_estimation([[1,1], [2,1], [1,2], [2,2], [3,5], [3,9], [3,10], [4,10], [4,11], [5,10], [7,10], [10,9], [10,6], [9,5], [10,5], [11,5], [9,4], [10,4], [11,4], [10,3]])

