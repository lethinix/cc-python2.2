import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("pokemon.csv")
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Attack", y="Defense", data=df, color="#0000ff") 
sns.regplot(x="Attack", y="Defense", data=df, scatter=False, color="red") # draw a regression line
plt.title("Attack vs. Defense")
plt.show()