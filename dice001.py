import random
import matplotlib.pyplot as plt

# 합의 빈도를 저장할 딕셔너리 (2~12까지 가능)
sum_counts = {i: 0 for i in range(2, 61)}

# 10000번 시뮬레이션
for _ in range(100000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)
    dice6 = random.randint(1, 6)
    dice7 = random.randint(1, 6)
    dice8 = random.randint(1, 6)
    dice9 = random.randint(1, 6)
    dice10 = random.randint(1, 6)
    
    total = dice1 + dice2+dice3+dice4+dice5+dice6+dice7+dice8+dice9+dice10
    sum_counts[total] += 1

# 결과 출력
for total, count in sum_counts.items():
    print(f"합 {total}: {count}번")

# 그래프 시각화
plt.bar(sum_counts.keys(), sum_counts.values(), color='green')
plt.title('Frequency of Sum of 10 Dice (10000 Times Simulation)')
plt.xlabel('Sum')
plt.ylabel('count')
plt.xticks(range(2, 61))  # x축 눈금 2~12
plt.show()
