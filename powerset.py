#alternative = (n!/(n-k!))

def powerset(x):
    if x == []:
        return [[]]
    return powerset(x[1:]) + [x[0:1] + y for y in powerset(x[1:])]

def count_powerset(x):
    return 2 ** x

def count_powerset_minus_one(x):
    return (2 ** x) - 1

print(count_powerset_minus_one(6))