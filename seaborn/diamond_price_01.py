import seaborn as sns
import matplotlib.pyplot as plt

data=sns.load_dataset("diamonds").sample(1000)

sns.boxenplot(
    data=data,
    x="cut",
    y="price"
)

plt.title("Diamon Price Distribution")
plt.xticks(rotation=20)
plt.show()

