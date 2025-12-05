import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import rc
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']

# 데이터 입력
data = [3,2,3,2,2,5,0,4,1,3,
        2,3,3,5,9,0,3,2,2,15,
        1,3,2,7,9,3,0,4,2,2]

# 각 값의 빈도 계산
freq = Counter(data)

# X축: ATM 사용 시간, Y축: 빈도
times = sorted(freq.keys())
counts = [freq[t] for t in times]

plt.figure(figsize=(10,6))

# 각 시간별로 원을 위로 쌓아 올리기
for x, count in zip(times, counts):
    for y in range(count):
        plt.scatter(x, y+1, s=200, c='black')  # 검은색 원

# 제목과 축 라벨
plt.title("ATM 사용 시간 도수분포 (검은색 원 아이콘)")
plt.xlabel("ATM 사용 시간")

# y축 제거 (눈금과 라벨 모두 없애기)
plt.yticks([])
plt.ylabel("")

# 외곽 테두리(spines) 제거, 단 x축(bottom)은 남기기
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(True)  # x축 선만 표시

# x축 눈금을 3의 배수만 표시
plt.xticks([0, 3, 6, 9, 12, 15])

plt.show()
