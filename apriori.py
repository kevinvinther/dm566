def apriori_gen(current, candidate, set):
    for i in set: 
        i += i
    
            
print(apriori_gen(2, 3, [["hi", "there"],[":)", "there"]]))