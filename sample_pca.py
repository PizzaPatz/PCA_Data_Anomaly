import numpy as np
from sklearn.decomposition import PCA
X = np.array([
				[-1, -1],
				[-2, -1],
				[-3, -2]
			])
''' Input '''
print(' Input: \n', X)
pca =  PCA(n_components = 2)
pca.fit(X)

print(' After fitting:')
print(pca.singular_values_)
