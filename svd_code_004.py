import numpy as np
m=6;n=16
condnum=42

U,r=np.linalg.qr(np.random.randn(m,m))
V,r=np.linalg.qr(np.random.randn(n,n))

s=np.linspace(condnum,1,np.min((m,n)))
S=np.zeros((m,n))

for i in range(min((m,n))):
    S[i,i]=s[i]
    
A=U@S@V.T
np.linalg.cond(A)