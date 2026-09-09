import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example: Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6],
    'D': [5, None, 1, 2, 3]  # Includes a missing value
}

df = pd.DataFrame(data)

# Handle missing values (optional: drop or fill)
df = df.fillna(df.mean(numeric_only=True))

# Compute correlation matrix
corr_matrix = df.corr(numeric_only=True)

# Set Seaborn style
sns.set(style="white")

# Create the heatmap
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,        # Show correlation values
    fmt=".2f",         # Format to 2 decimal places
    cmap="coolwarm",   # Color map
    vmin=-1, vmax=1,   # Fix scale from -1 to 1
    linewidths=0.5,    # Grid lines
    cbar_kws={"shrink": 0.8}  # Color bar size
)

# Title
plt.title("Correlation Matrix Heatmap", fontsize=14, pad=12)

# Show plot
plt.tight_layout()
plt.show()