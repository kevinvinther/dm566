def Apriori(i, D, delta):
    """
    Apriori candidate generation
    i: current itemset
    D: database
    delta: minimum support
    frequent_1_itemsets: frequent 1-itemsets
    """
    k = 2
    while frequen_1_itemsets[k-1] != []:
        c[k] = AprioriGenerateCandidates(S[k-1]);
        for transaction in D:
            C[transaction] = if (c[k] in C[transaction])
        k += 1

