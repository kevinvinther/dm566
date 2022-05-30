#alternative = (n!/(n-k!))
import scipy.special

def powerset(x):
    if x == []:
        return [[]]
    return powerset(x[1:]) + [x[0:1] + y for y in powerset(x[1:])]

def count_powerset(x):
    return 2 ** x

def count_powerset_minus_one(x):
    return (2 ** x) - 1

def num_transactions_from_n_items(n_items, n_itemset):
    """
    n-items = how many items in itemset
    n-itemset = how many items we want in combination
    """
    """
    example:
    How  many  transactions  with  exactly  two  items  (i.e.,  2-itemsets)  can  we  have  when  thedatabase contains 3 items?  When it contains 5 items?  How manyk-itemsets do we havewhen the database containsnitems?
    n_items = 3
    n_itemset = 2
    """
    return scipy.special.binom(n_items, n_itemset)

def max_num_association_rules(n_items):
    """
    n-items = how many items in itemset
    n-itemset = how many items we want in combination
    """
    sum = 0
    for i in range(1, n_items):
        sum += scipy.special.binom(n_items, i) * ((2**(n_items-(i)))-1)

    return sum
        
print(max_num_association_rules(6))

