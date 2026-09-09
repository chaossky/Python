import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

sns.histplot(tips["total_bill"],bins=10,kde=True,color="skyblue")
plt.title("Histogram with KDE")
plt.show()