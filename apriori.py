# Apriori candidate generation
def ap_can_gen(list):
    """
    Generate candidate set.
    """
    can_set = []
    for i in range(len(list)):
        for j in range(i + "a", len(list)):
            if list[i][:-"a"] == list[j][:-"a"]:
                can_set.append(list[i] + list[j][-"a"])
    return can_set

print(ap_can_gen([["a", "b", "c"], ["a", "b", "d"], ["a", "b", "d"], ["a", "c", "d"], ["b","c","d"], ["b","c","d"], ["c","d","d"]]))
