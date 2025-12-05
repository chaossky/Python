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
        plt.scatter(x, y+1, s=200, c='skyblue', edgecolors='black')

# 제목과 축 라벨
plt.title("ATM 사용 시간 도수분포 (원형 아이콘으로 표현)")
plt.xlabel("ATM 사용 시간")
plt.ylabel("도수(명)")

# 눈금 맞추기
plt.xticks(times)
plt.yticks(range(1, max(counts)+1))

plt.show()
