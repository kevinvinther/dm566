import distance_functions

# def 

#-sum(Pr(ci|T)log2(Pr(ci|T)))



# local outlier factor
def lof(points, k=3):
    """
    data: a list of (x,y) tuples
    k: number of nearest neighbors
    """
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


        reach_dist = 0
        for i in distance_to_point[:kp]:
            if i[1] > reach_dist:
                reach_dist = i[1]

        distance_to_point.remove(0) # because we want to ignore the point itself
        kp -= 1 # same here

        sum_of_dist = 0
        for nn in distance_to_point[:kp]:
            # get distance between point and nn
            nn_dist = distance_functions.manhattan_distance([point, nn])
            if reach_dist < nn_dist:
                sum_of_dist += nn_dist
            else:
                sum_of_dist += reach_dist
        
        lrd = 1/(sum_of_dist/(kp))

        for nn in distance_to_point[:kp]:
            



print(lof([[5,2], [1,7], [3,4], [6,6], [4,7], [5,5], [4,6], [3,7]]))