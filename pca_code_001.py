import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. 데이터 생성
# -----------------------------
N = 1000  # 샘플 개수
# 키(height) 데이터: 150~190cm 범위의 선형 값 + 약간의 노이즈
h = np.linspace(150, 190, N) + np.random.randn(N) * 5
# 몸무게(weight) 데이터: 키와 선형 관계(0.7*h - 50) + 노이즈
w = h * 0.7 - 50 + np.random.randn(N) * 10

# -----------------------------
# 2. 공분산 행렬 계산
# -----------------------------
# 데이터 행렬 X: (N x 2) 형태, 각 행은 [키, 몸무게]
X = np.vstack((h, w)).T
# 평균을 빼서 중심화(centering): PCA는 평균이 0인 데이터에 적용
X = X - np.mean(X, axis=0)
# 공분산 행렬 C 계산
# (X.T @ X) / (N-1) 형태로 계산
C = X.T @ X / (len(h) - 1)

# -----------------------------
# 3. PCA 수행
# -----------------------------
# 공분산 행렬의 고유값(eigenvalue)과 고유벡터(eigenvector) 계산
eigvals, V = np.linalg.eig(C)
# 고유값을 내림차순으로 정렬 (가장 큰 분산 방향이 첫 번째 주성분)
i = np.argsort(eigvals)[::-1]
V = V[:, i]          # 정렬된 고유벡터
eigvals = eigvals[i] # 정렬된 고유값
# 각 고유값이 전체 분산에서 차지하는 비율(%) 계산
eigvals = 100 * eigvals / np.sum(eigvals)
# 주성분 점수(scores): 원 데이터 X를 주성분 좌표계로 변환
scores = X @ V  # 여기서는 사용하지 않지만, PCA 결과 활용 가능

# -----------------------------
# 4. 데이터와 주성분 시각화
# -----------------------------
fig = plt.figure(figsize=(5, 5))
# 원 데이터 산점도 (검은 점)
plt.plot(X[:, 0], X[:, 1], 'ko')
# 첫 번째 주성분 벡터(빨간 선, 길이 45로 스케일링)
plt.plot([0, V[0, 0] * 45], [0, V[1, 0] * 45], 'r')
# 두 번째 주성분 벡터(빨간 선, 길이 25로 스케일링)
plt.plot([0, V[0, 1] * 25], [0, V[1, 1] * 25], 'r')
# 축 라벨 및 범위 설정
plt.xlabel('Height')
plt.ylabel('Weight')
plt.axis([-50, 50, -50, 50])
plt.show()
