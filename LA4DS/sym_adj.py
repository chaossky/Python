from sympy import Matrix

A=Matrix([[1,2,3],
          [0,4,5],
          [1,0,6]])

print("Sympy adj(A):")
print(A.adjugate())