import seaborn as sns
import pandas as pd

data = {
    "total_bill": [16.99, 10.34, 21.01, 23.69, 24.59, 15.42, 18.30, 22.15, 19.80, 17.25],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 2.50, 3.00, 2.75],
    "day": ["Sun"]*4 + ["Sat"]*3 + ["Thur"]*3,
    "sex": ["Female", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female"],
    "size": [2, 3, 3, 2, 4, 4, 2, 4, 2, 2]
}

df = pd.DataFrame(data)
print(df.head(10))
