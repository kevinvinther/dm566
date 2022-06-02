import math

# Look at solution sheet 09 for an example of how to do this

def entropy(a, b):
    sum = a + b
    return -(((a/sum)*math.log2(a/sum)) + ((b/sum)*math.log2(b/sum)))

# T = the total result from all the entropys
def information_gain(T, T_entropies, list):
    summation = 0.0
    for i in range(len(list)):
        summation += (T_entropies[i]/sum(T_entropies))*list[i]

    return T - summation 






print(entropy(1, 2)) # = 0.918
print(entropy(2, 1)) # = 0.918
print(entropy(1, 1)) # = 1
print(information_gain(1, [3.0, 3.0, 2.0], [0.918, 0.918, 1]))
