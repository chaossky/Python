import pandas as pd
df=pd.DataFrame({
    "Name":["A","B","C","D","E"],
    "Score":[78,95,83,91,88]
})

df=df.sort_values("Score",ascending=False)
df["Rank"]=range(1,len(df)+1)

df.style \
    .background_gradient(subset=["Score"]) \
    .highlight_min(subset=["Score"])
    
print(df)    
