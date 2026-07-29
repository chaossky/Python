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

def show_permutations(matrix):
    """행렬의 모든 순열과 부호, π 매핑을 출력"""
    n = len(matrix)
    for perm in itertools.permutations(range(n)):
        sign = permutation_sign(perm)
        mapping = {f"π({i+1})": perm[i]+1 for i in range(n)}  # 자리 번호 → 원소 번호
        print(f"순열: {perm}, 부호: {sign}, 매핑: {mapping}")

# 4×4 행렬 예시
A4 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

show_permutations(A4)
