import numpy as np

def minor(matrix,i,j):
    sub_matrix=np.delete(np.delete(matrix,i,axis=0),j,axis=1)
    return np.linalg.det(sub_matrix)

def cofactor_matrix(matrix):
    n=matrix.shape[0]
    C=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            C[i,j]=((-1)**(i+j))*minor(matrix,i,j)
    return C

def adjugate(matrix):
    return cofactor_matrix(matrix).T

A=np.array([[1,2,3],
            [0,4,5],
            [1,0,6]])

print("Numpy adj(A):")
print(adjugate(A))