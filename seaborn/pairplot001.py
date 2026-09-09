import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.pairplot(tips,hue="sex",palette="coolwarm")
plt.show()