import numpy as np
import matplotlib.pyplot as plt
from imageio.v2 import imread

pic = imread('duck.jpeg')
pic = np.array(pic, dtype=float)

# full_matrices=False 옵션을 반드시 줘야 차원 맞음
U, s, Vt = np.linalg.svd(pic, full_matrices=False)

# 대각행렬 S 생성
S = np.diag(s)

# 원하는 rank 선택
comps = 21
lowrank = U[:, :comps] @ S[:comps, :comps] @ Vt[:comps, :]

plt.subplot(1, 2, 1)
plt.imshow(pic, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(lowrank, cmap='gray')
plt.title(f'Rank {comps} Approximation')

plt.show()
