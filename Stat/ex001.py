import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import rc

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']

data=[
     "A", "B", "B", "A", "C", "B", "C", "C", "C", "A",
    "C", "B", "C", "A", "C", "C", "B", "C", "C", "A",
    "A", "B", "C", "C", "B", "C", "B", "A", "C", "A"
]

freq=Counter(data)

# 원형 그래프
plt.figure(figsize=(6,6))
plt.pie(freq.values(),labels=freq.keys(),autopct='%1.1f%%',
        startangle=90,colors=['skyblue','lightgreen','salmon'])
plt.title("스마트폰 종류별 도수 분포(원형그래프)")

# plt.bar(freq.keys(),freq.values(),color=['skyblue','lightgreen','salmon'])
# plt.title("스마트폰 종류별 도수분포")
# plt.xlabel("스마트폰 종류")
# plt.ylabel("도수")
# plt.grid(axis='y',linestyle='--',alpha=0.7)

plt.show()