def union(list1, list2):
    return list(set(list1) | set(list2))

def intersection(list1, list2):
    return list(set(list1) & set(list2))

def not_in(list1, list2):
    return list(set(list1) - set(list2))

def cartesian_product(list1, list2):
    return [(x, y) for x in list1 for y in list2]

def power_set(list1):
    return list(set(list1))

def power_set_with_duplicates(list1):
    return list(set(list1))



print(intersection([1, 2, 3], [2, 3, 4]))
