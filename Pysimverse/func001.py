import numpy as np

# 0에서 1까지 5개의 값 생성 (끝 값 포함)
arr1 = np.linspace(0, 1, 5)
print(arr1)
# 출력: [0.   0.25 0.5  0.75 1.  ]

# 0에서 1까지 5개의 값 생성 (끝 값 제외)
arr2 = np.linspace(0, 1, 5, endpoint=False)
print(arr2)
# 출력: [0.  0.2 0.4 0.6 0.8]

# 간격(step)도 함께 반환
arr3, step = np.linspace(0, 1, 5, retstep=True)
print(arr3, step)
# 출력: [0.   0.25 0.5  0.75 1.  ] 0.25
