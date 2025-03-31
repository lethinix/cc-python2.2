# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://openei.org/wiki/Wind_Turbine_Data"
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(response.text, "html.parser")

# # Extract all tables (Pandas auto-detects them)
# tables = pd.read_html(url)
# turbine_table = tables[0]  # First table on the page

# # Save to CSV
# turbine_table.to_csv("openEI_turbine_table.csv", index=False)
# print("✅ Table saved as 'openEI_turbine_table.csv'")

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://openei.org/wiki/Wind_Turbine_Data"
response = requests.get(url, verify=False)  # Temporarily ignores SSL
soup = BeautifulSoup(response.text, 'html.parser')
tables = pd.read_html(str(soup))  # Parse tables
print(tables[0].head())