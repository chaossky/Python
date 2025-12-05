import matplotlib.pyplot as plt
from matplotlib import rc
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']

# 데이터 입력
data = [3,2,3,2,2,5,0,4,1,3,
        2,3,3,5,9,0,3,2,2,15,
        1,3,2,7,9,3,0,4,2,2]

# 점도표 그리기
plt.figure(figsize=(10, 4))
plt.plot(data, [1]*len(data), 'o', markersize=8)  # y축은 모두 1로 고정, 점만 표시
plt.yticks([])  # y축 눈금 제거
plt.xlabel("ATM 사용 시간")
plt.title("ATM 사용 시간 점도표")

plt.show()