import itertools

def permutation_sign(perm):
    """순열의 부호(+1 또는 -1)를 계산"""
    inv_count = 0
    n = len(perm)
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inv_count += 1
    return -1 if inv_count % 2 else 1

def determinant(matrix):
    """n×n 행렬식 계산"""
    n = len(matrix)
    det = 0
    for perm in itertools.permutations(range(n)):
        sign = permutation_sign(perm)
        product = 1
        for i in range(n):
            product *= matrix[i][perm[i]]
        det += sign * product
    return det

# 2×2 예시
A2 = [[1, 2],
      [3, 4]]
print("det(A2) =", determinant(A2))  # 결과: -2

# 3×3 예시
A3 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print("det(A3) =", determinant(A3))  # 결과: 0
