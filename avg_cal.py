import numpy as np

data = np.array([1, 2, 3, 4])

# np.mean: 단순 평균
print(np.mean(data))  
# 출력: 2.5

# np.average: 단순 평균 (weights 없음)
print(np.average(data))  
# 출력: 2.5

# np.average: 가중 평균
weights = np.array([1, 1, 2, 2])  # 뒤쪽 값에 더 큰 가중치
print(np.average(data, weights=weights))  
# 출력: 3.166...
