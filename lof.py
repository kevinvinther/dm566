import distance_functions

# def 

#-sum(Pr(ci|T)log2(Pr(ci|T)))

# This functions finds both the lof and kdist for a list of points
# If you want to take the point itself in the list, remove lines 42 and 43

# local outlier factor
def lof(points, k=2):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    iterator = -1
    k += 1
    lrds = []
    knns = []
    for point in points:
        iterator += 1
        iterator_for_point_2 = 0
        distance_to_point = dict()
        # find the k nearest neighbors
        # we will only use this if we're not given epsilon
        for point2 in points:
            distance_to_point[iterator_for_point_2] = round(distance_functions.manhattan_distance([point, point2]), 2)
            iterator_for_point_2 += 1
        print(distance_to_point)

        value = (sorted(distance_to_point.items(), key=lambda x: x[1])[k - 1])

        value_amount = sum([1 for i in distance_to_point.values() if i == value[1]])

        distance_to_point = sorted(distance_to_point.items(), key=lambda x: x[1])

        value_in_list = 0
        
        for i in distance_to_point[:k]:
            if i[1] == value[1]:
                value_in_list += 1

        kp = k + (value_amount - value_in_list)

        distance_to_point.pop(0) # because we don't want to count the first point
        kp -= 1 # same here


        # kdist(distance_to_point[:kp])



        # sum_of_dist = 0
        # for point2 in distance_to_point[:kp]:
        #     # get distance between point and nn
        #     nn_dist = point2[1]
        #     if reach_dist < nn_dist:
        #         sum_of_dist += nn_dist
        #     else:
        #         sum_of_dist += reach_dist
        knns.append(distance_to_point[:kp])
        # lrds.append(1/(sum_of_dist/(kp)))
        # print("1/" + str(sum_of_dist) + "/" + str(kp))

    lofs = []
    for i in range(len(knns)):
        lofs.append(lof_calc(knns[i], knns, i))

    kdists = []
    for i in range(len(knns)):
        kdists.append(kdist(knns[i]))
    return (lofs, kdists)
    

def kdist(knn):
    dist = 0
    for i in knn:
        dist = max(dist, i[1])
    return dist

def reachdist(distance, kdist):
    return max(distance, kdist) 

def lrd(current_knn, knns):
    sum = 0
    for i in current_knn:
        sum += reachdist(i[1], kdist(knns[i[0]]))

    return (1/ (sum / len(current_knn)))

def lof_calc(current_knn, knns, k):
    sum = 0
    for i in current_knn:
        sum += (lrd(knns[i[0]], knns) / lrd(knns[k], knns))

    return sum / len(current_knn)

            
#   kdist(o) = kNN(o).distance_to_last_elem()

#   reachdist(A, C) = MAX(dist(A, C), kdist(C))

#   lrd(p) = 1/(sum_kNN(p){reachdist(p, o)} / Cardinality(kNN(p)))

#   LOF(A) = (sum_kNN(A){lrd(o) / lrd(A)}) / (Cardinality(kNN(p)))


print(lof([[5,2], [1,7], [3,4], [6,6], [4,7], [5,5], [4,6], [3,7]]))