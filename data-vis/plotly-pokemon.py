import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

fig = px.scatter(df, x="Attack", y="Speed", color="Type 1", hover_name="Name", title="Pokémon Attack vs. Speed")
fig.show()