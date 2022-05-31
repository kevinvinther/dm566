import numpy as np
import math 
mu_a = np.matrix('2 2')
sigma_a = np.matrix('3 0; 0 3') 

size = 0.3

p = np.matrix('2.5 3')


dist2 = np.matmul(np.matmul((p - mu_a), np.linalg.inv(sigma_a)), (p - mu_a).T)

dens = 1/(math.sqrt((2 * math.pi)**2 * np.linalg.det(sigma_a))) * math.exp(-0.5 * dist2)

print('dist2: ' + str(dist2))
print('dens: ' + str(dens))
print('score: ' + str(dens * size))
print(' remember to get the sum of all scores to see which is best !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
