import numpy as np
A=[[1,1,0],[0,1,1]]
U,s,V=np.linalg.svd(A)

print(U)
print(s)
print(V)