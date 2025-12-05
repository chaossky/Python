import matplotlib.pyplot as plt

from matplotlib import rc
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']

sports_data={"농구":10, "야구":7,"미식축구":6,"축구":5,"테니스":5,"하키":2}

sports=list(sports_data.keys())
counts=list(sports_data.values())

plt.bar(sports,counts, color='skyblue',edgecolor='black')

plt.title("가장 좋아하는 운동 도수 분포")
plt.xlabel("운동")
plt.ylabel("학생 수")

for i,count in enumerate(counts):
    plt.text(i, count+0.2,str(count), ha='center')

plt.show()

