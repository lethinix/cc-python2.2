import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df2 = pd.read_csv("ozone_2024/ozone_2024.csv")
top_ozone = df2.nlargest(20, "OZONE").reset_index(drop=True)

# combine site and date labels
top_ozone["SITE_DATE"] = (
    top_ozone["SITE_ID"] + "\n" +  # Newline for readability
    pd.to_datetime(top_ozone["DATE_TIME"]).dt.strftime("%b-%d %H:%M")
)

# bar graph
plt.figure(figsize=(18, 8))
sns.barplot(
    data=top_ozone,
    x="SITE_DATE",  
    y="OZONE",
    palette="viridis"
)


plt.xticks(rotation=45, ha='right', fontsize=10)  
plt.title("top 20 ozone values across all sites", fontweight='bold')
plt.xlabel("site ID and date/time", fontsize=12)
plt.ylabel("ozone concentration (ppm)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.tight_layout()
plt.show()