from sympy import Matrix 
A=Matrix([[2,-1,1],[1,2,-1],[3,1,1]]) 
b=Matrix([2,3,7])
print(A.LUsolve(b))
