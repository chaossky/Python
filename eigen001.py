import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import hankel

t = np.arange(1, 51)
lstrow = np.append(t[-1], np.arange(1, t[-1]))
H = hankel(t, r=lstrow)
d, V = np.linalg.eig(H)
V = V[:, np.argsort(d)[::-1]]

plt.subplot(221)
plt.imshow(H)
plt.title("Hankel Matrix")

plt.subplot(222)
plt.imshow(V.real)  # 고유벡터는 복소수일 수 있으므로 .real 사용
plt.title("Eigenvectors")

plt.subplot(212)
plt.plot(V[:, :4].real)
plt.title("First 4 Eigenvectors")

plt.tight_layout()
plt.show()   # 반드시 추가!
