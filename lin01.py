import numpy as np
asList=[1,2,4]
asArray=np.array([1,2,4])
rowVec=np.array([[1,2,4]])
colVec=np.array([[1],[2],[4]])

print(f'asList :  {np.shape(asList)}')
print(f'asArray : {asArray.shape}')
print(f'rowVec : {rowVec.shape}')
print(f'colVec : {colVec.shape}')
v=np.array([[4,5,6]])
w=np.array([[10,20,30]]).T
u=np.array([0,3,6,9])
vPlusW=v+w
print(f'vPlusW : {vPlusW}')
#uplusW=u+w

s=2
a=[3,4,5]#asList
b=np.array(a)#asArray
print(a*s)
print(b*s)
#print(a+s)
print(b+s)