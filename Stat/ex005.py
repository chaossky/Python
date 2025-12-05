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

# X축: ATM 사용 시간, Y축: 빈도(도수)
times = list(freq.keys())
counts = list(freq.values())

# 막대 그래프 그리기
plt.bar(times, counts, color='skyblue', edgecolor='black')

# 제목과 축 라벨 추가
plt.title("ATM 사용 시간 도수분포 (막대 그래프)")
plt.xlabel("ATM 사용 시간")
plt.ylabel("도수(명)")

# 값 표시 (각 막대 위에 빈도 표시)
for i, count in zip(times, counts):
    plt.text(i, count + 0.1, str(count), ha='center')

plt.show()
