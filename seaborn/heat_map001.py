import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("D:\\DevOPS\\Python\\seaborn\\bestsellers with categories.csv")
co_mtx=data.corr(numeric_only=True)
# tips=sns.load_dataset("tips")
# corr=tips.corr()

sns.heatmap(co_mtx,annot=True,cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.show()