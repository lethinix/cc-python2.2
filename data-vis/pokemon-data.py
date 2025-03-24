import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("pokemon.csv")
#print(df.info())
#print(df["Type 1"].value_counts())
print(df["Type 1"].value_counts().index) # gives the unique values under each type 
print(df["Type 1"].value_counts().values)

unique_types = df["Type 1"].value_counts().index 
type_count = df["Type 1"].value_counts().values

colors = sns.color_palette("tab20", n_colors=len(unique_types))

plt.figure(figsize=(10,5))
plt.bar(unique_types, type_count, color=colors)
plt.xlabel("type 1")
plt.ylabel("count")
plt.title("distribution of pokemon by type1")
plt.xticks(rotation=45)


selected_types = ["Fire", "Water", "Grass", "Electric"]
filtered_df = df["Type 1"].isin(selected_types)

sns.scatterplot()

plt.show()

