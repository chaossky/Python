import numpy as np
A=np.random.randn(4,5)
print(A)
L2,V=np.linalg.eig(A.T@A)
print(L2)
print(V)
V=V[:,np.argsort(L2)[::-1]]
print(V)
L2,U=np.linalg.eig(A@A.T)
print(L2)
print(U)
U=U[:,np.argsort(L2)[::-1]]
print(U)

S=np.zeros(A.shape)
for i ,s in enumerate(np.sort(L2[::-1])):
    S[i,i]=np.sqrt(s)
    
print(S)
U2,S2,V2=np.linalg.svd(A)

print(U2)
print(S2)
print(V2)