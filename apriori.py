# apriori candidate generation

from sklearn.cluster import k_means


def apriori_candidate_generation(itemsets):
    # itemsets: list of itemsets
    # return: list of candidate itemsets
    
    # initialize
    candidates = []
    # sort itemsets by length
    itemsets.sort(key=lambda x: len(x))
    # loop over itemsets
    for i in range(len(itemsets)):


print(apriori_candidate_generation([[1,2,3],
                             [1,2,4],
                             [1,2,5],
                             [1,3,4],
                             [1,3,5],
                             [2,3,4],
                             [2,3,5],
                             [3,4,5]]))