import numpy as np
from sklearn.neighbors import LocalOutlierFactor

x = np.array([[5,2], [1,7], [3,4], [6,6], [4,7], [5,5], [4,6], [3,7]])

clf = LocalOutlierFactor(n_neighbors=2, metric='manhattan')
y_pred = clf.fit_predict(x)
scores = clf.negative_outlier_factor_
print(-scores)