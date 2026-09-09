import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = pd.DataFrame({
'A': [1, 2, 3, 4, 5],
'B': [5, 4, 3, 2, 1],
'C': [2, 3, 4, 5, 6]
})

# Compute correlation matrix
corr_matrix = data.corr()

# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()