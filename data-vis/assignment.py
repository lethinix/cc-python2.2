import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df2 = pd.read_csv("ozone_2024/ozone_2024.csv")


top_ozone = df2[df2["SITE_ID"] == "ABT147"].nlargest(20, "OZONE").reset_index(drop=True)

# convert DATE_TIME
top_ozone["DATE_SHORT"] = pd.to_datetime(top_ozone["DATE_TIME"]).dt.strftime("%b-%d %H:%M")

# bar graph
plt.figure(figsize=(15, 8))
sns.barplot(
    data=top_ozone,
    x="DATE_SHORT",  
    y="OZONE",
    palette="viridis"
)

plt.xticks(rotation=45, ha='right')
plt.title("top 20 ozone values at site ABT147 - dated")
plt.xlabel("date and time")
plt.ylabel("ozone concentration (ppm)")
plt.tight_layout()  # Prevent label cutoff
plt.show()