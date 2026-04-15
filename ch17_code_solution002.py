import numpy as np

n=4
nIterations=500
defcat=np.zeros(nIterations)

for iteri in range(nIterations):
    A=np.random.randint(-10,11,size=(n,n))
    e=np.linalg.eig(A)[0]
    while ~np.all(np.isreal(e)):
        A=np.random.randint(-10,11,size=(n,n))
        e=np.linalg.eig(A)[0]
        
    t=n*np.spacing(np.max(np.linalg.svd(A)[1]))
    
    if np.all(np.sign(e)==1):
        defcat[iteri]=1
    elif np.all(np.sign(e)>-1)&sum(abs(e)<t)>0:
        defcat[iteri]=2
    elif np.all(np.sign(e)<1)&sum(abs(e)<t)>0:
        defcat[iteri]=4
    elif np.all(np.sign(e)==-1):
        defcat[iteri]=5
    else:
        defcat[iteri]=3
        
    for i in range(1,6):
        print('cat %g: %g'%(i ,sum(defcat==i)))