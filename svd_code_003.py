import matplotlib.pyplot as plt   # 그래프와 그림을 그리기 위한 matplotlib 라이브러리 불러오기
import numpy as np                # 수치 계산을 위한 numpy 라이브러리 불러오기

fig, ax = plt.subplots(2, 4)      # 2행 4열의 그래프 영역(subplot) 생성, fig는 전체 그림, ax는 각 칸

A = np.random.randn(5, 3)         # 5x4 크기의 랜덤 행렬 생성 (정규분포 난수)
U, s, V = np.linalg.svd(A)        # 행렬 A에 대해 SVD 분해 수행 → U, 특이값 s, V 반환
S = np.diag(s)                    # 특이값 벡터 s를 대각행렬로 변환하여 S 생성

for i in range(3):                # 첫 번째 3개의 특이값/벡터에 대해 반복
    onelayer = np.outer(U[:, i], V[i, :]) * s[i]   # i번째 특이값과 대응하는 U, V 벡터로 한 층(layer) 구성
    ax[0, i].imshow(onelayer)     # 위쪽 행(0행)의 i번째 칸에 해당 layer를 그림으로 표시
    ax[0, i].set_title('Layer %g' % i)  # 제목: Layer i
    ax[0, i].axis('off')          # 축 눈금과 테두리 제거
    
    lowrank = U[:, :i+1] @ S[:i+1, :i+1] @ V[:i+1, :]   # i번째까지 누적한 저랭크 근사 행렬 계산
    ax[1, i].imshow(lowrank)      # 아래쪽 행(1행)의 i번째 칸에 누적 근사 행렬 표시
    ax[1, i].set_title('Layers 0:%g' % i)  # 제목: Layers 0~i
    ax[1, i].axis('off')          # 축 눈금과 테두리 제거
    
ax[1, 3].imshow(A)                # 마지막 칸(1행 3열)에 원래 행렬 A 표시
ax[1, 3].set_title('Orig. A')     # 제목: 원래 행렬 A
ax[1, 3].axis('off')              # 축 눈금과 테두리 제거
ax[0, 3].axis('off')              # 위쪽 마지막 칸은 비워두고 축 제거

plt.show()                        # 모든 그래프를 화면에 출력
