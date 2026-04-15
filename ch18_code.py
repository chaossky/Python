import numpy as np
n=200
X=np.random.randn(n,4) # data
X=X-np.mean(X,axis=0) # mean-centered

covM=X.T@X/(n-1) #covariance
stdM=np.linalg.inv(np.diag(np.std(X,axis=0,ddof=1))) #stdevs
corM=stdM@X.T@X@stdM/(n-1)

# compare ours against numpy's
print(np.round(covM-np.cov(X.T),3))
print(np.round(corM-np.corrcoef(X.T),3))