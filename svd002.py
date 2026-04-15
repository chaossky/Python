import numpy as np
A=np.random.randn(5,5)
# A=np.random.randint(3,3)
print(A)
s=np.linalg.svd(A)[1]
condnum=np.max(s)/np.min(s)

print(condnum,np.linalg.cond(A))