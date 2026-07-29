import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery') 
'''
plt.style.use() 는 Matplotlib에서 그래프의 전반적인 스타일(색상, 폰트, 배경, 선 모양 등)을 한 번에 적용할 수 있게 해주는 함수입니다.

CSS처럼 미리 정의된 테마를 불러오거나, 직접 만든 스타일 파일(.mplstyle)을 적용할 수 있습니다.
'''

x=np.linspace(0,10,100)
y=4+1*np.sin(2*x)
x2=np.linspace(0,10,25)
y2=4+1*np.sin(2*x2)

# plot
fig, ax = plt.subplots()
ax.plot(x2,y2+2.5,'x',markeredgewidth=2)
ax.plot(x,y,linewidth=2)
ax.plot(x2,y2-2.5,'o-',markeredgewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0,8), yticks=np.arange(1, 8))

plt.show()

