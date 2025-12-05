import stemgraphic
import matplotlib.pyplot as plt

# 데이터 입력
data = [56, 89, 165, 73, 83, 145, 90, 189, 127, 77, 110, 112, 132,
        120, 94, 130, 84, 65, 99, 154, 86, 120, 122, 103, 130]

stemgraphic.stem_graphic(data,scale=10)
plt.show()

