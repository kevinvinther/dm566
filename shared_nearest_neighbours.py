import distance_functions

def shared_nearest_neighbours(points):
    k = 5  # number of nearest neighbors (includes self), remember to +1
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    iterator = -1
    for point in points:
        iterator += 1
        iterator_for_point_2 = 0
        distance_to_point = dict()
        # find the k nearest neighbors
        # we will only use this if we're not given epsilon
        for point2 in points:
            distance_to_point[str(alphabet[iterator_for_point_2]) ] = round(distance_functions.manhattan_distance([point, point2]), 2)
            iterator_for_point_2 += 1

        value = (sorted(distance_to_point.items(), key=lambda x: x[1])[k -1 ])

        value_amount = sum([1 for i in distance_to_point.values() if i == value[1]])

        distance_to_point = sorted(distance_to_point.items(), key=lambda x: x[1])

        value_in_list = 0
        
        for i in distance_to_point[:k]:
            if i[1] == value[1]:
                value_in_list += 1

        kp = k + (value_amount - value_in_list)

        print(distance_to_point[:kp])
        

shared_nearest_neighbours([[1,1], [2,1], [1,2], [2,2], [3,5], [3,9], [3,10], [4,10], [4,11], [5,10], [7,10], [10,9], [10,6], [9,5], [10,5], [11,5], [9,4], [10,4], [11,4], [10,3]])
