import math
import random
import matplotlib.pyplot as plt

numbers = [1,2,3,4,5,6]
print("How many dice do you want to roll?")
n = int(input())
results = dict()

print("How many times do you want to roll the dice?")
m = int(input())


plt.style.use('ggplot')

for i in range (1,m+1):
    new_number = 0
    for j in range (1,n+1):
        new_number += random.choice(numbers)

    results[new_number] = results.get(new_number, 0) + 1
    print(i)

results = (dict(sorted(results.items())))
    
plt.bar(range(len(results)), list(results.values()), align='center')
plt.xticks(range(len(results)), list(results.keys()))
plt.show()
