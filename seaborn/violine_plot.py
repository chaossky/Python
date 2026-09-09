import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill",hue="sex",data=tips,split=True,palette="Set1")
plt.title("Violine Plot Example")
plt.show()