def classifier(characters, list):
    true_positives = {}
    false_positives = {}
    false_negatives = {}    

    for c in characters:
        for i in list:
            sum = 'TN'
            if i[0] == c and i[1] == c: # true positive
                sum = 'TP'
                true_positives[c] = true_positives.get(c, 0) + 1
            elif i[0] != c and i[1] == c: # false positive
                sum = 'FP'
                false_positives[c] = false_positives.get(c, 0) + 1
            elif i[0] == c and i[1] != c: # false negative
                sum = 'FN'
                false_negatives[c] = false_negatives.get(c, 0) + 1
            elif i[0] != c and i[1] != c: # true negative
                sum = 'TN'
            print(str(i[0]) + ' ' + str(i[1]) + ': ' + sum + ' w.r.t ' + c)
    print('True positives: ' + str(true_positives))
    print('False positives: ' + str(false_positives))
    print('False negatives: ' + str(false_negatives))     

    # Calculate precision and recall
    precision = {}
    recall = {}
    for c in characters:
        if true_positives.get(c, 0) != 0:
            precision[c] = true_positives.get(c, 0) / (true_positives.get(c, 0) + false_positives.get(c, 0))
            print('Precision of ' + c + ': ' + str(true_positives.get(c,0)) + ' / ' + '(' + str(true_positives.get(c,0))
             + ' + ' + str(false_positives.get(c,0)) + ')\n')
        else:
            precision[c] = 0
        if true_positives.get(c, 0) != 0:
            recall[c] = true_positives.get(c, 0) / (true_positives.get(c, 0) + false_negatives.get(c, 0))
            print('Recall of ' + c + ': ' + str(true_positives.get(c,0)) + ' / ' + '(' + str(true_positives.get(c,0))
             + ' + ' + str(false_negatives.get(c,0)) + ')\n')
        else:
            recall[c] = 0
    print('Precision: ' + str(precision))
    print('Recall: ' + str(recall))

    #F1 (the harmonic mean of precision and recall)
    for cluster in characters:
        print('(2 * ' + str(recall[cluster]) + ' * ' + str(precision[cluster]) + ') / (' + str(recall[cluster]) + ' + ' + str(precision[cluster]) + ')')
        f1 = (2 * recall[cluster] * precision[cluster]) / (recall[cluster] + precision[cluster])
        print('F1 = ' + str(f1) + ', ' + str(cluster))

# first class is the actual the second is the predicted 
classifier(['a', 'b', 'c'], [['a','a'], ['b','a'], 
            ['c','c'], ['b','c'], ['a','b'], 
            ['b','b'], ['c', 'a'], ['a','a'], ['a','a'],
            ['b','c'], ['b','a'], ['c','a'], ['a','b'], ['c','c'],
            ['b','b'], ['c','b'], ['a','a'], ['b','b'],
            ['c','c'], ['a','b']])
