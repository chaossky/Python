import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",data=tips,palette="Set2")
plt.title("Box Plot Example")
plt.show()