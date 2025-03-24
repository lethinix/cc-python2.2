import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")
top_attack_pokemon = df.nlargest(10, "Attack")

fig = px.bar(
    top_attack_pokemon, 
    x="Name", 
    y="Attack", 
    color="Name",  
    title="Top 10 Pokémon with Highest Attack",
    labels={"Attack": "Attack value", "Name": "Pokemon"},
)

fig.show()