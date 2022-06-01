from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np

X = np.array([[5,3], [1,3], [1,8], [1,9], [4,6], [5,4], [5,7], [6,1], [6,3], [6,6], [6,8], [7,2], [7,4], [7,6], [8,2], [8,3]])
nbrs = KNeighborsClassifier(n_neighbors=2, algorithm='ball_tree').fit(X)
