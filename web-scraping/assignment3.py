import requests
import bs4
import pandas as pd

response = requests.get("https://www.worldometers.info/")
soup = bs4.BeautifulSoup(response.text, "html.parser")

# Initialize lists for BOTH metrics
forest_data = []
co2_data = []

for item in soup.select(".counter-group"):  # Changed selector to target counters
    title = item.select_one(".counter-title").text.strip() if item.select_one(".counter-title") else ""
    value = item.select_one(".counter-number").text.strip() if item.select_one(".counter-number") else ""
    
    # Filter for specific metrics (case-insensitive)
    if "forest" in title.lower():
        forest_data.append(value)
    elif "co2" in title.lower():
        co2_data.append(value)

# Create DataFrame with your original structure
heading_df = pd.DataFrame()
heading_df["Forest Lost This Year"] = pd.Series(forest_data).values
heading_df["CO2 Emissions This Year"] = pd.Series(co2_data).values

print(heading_df)
heading_df.to_csv("environmental.csv", index=False)  # Export with your original filename

# # import requests
# # import bs4
# # import pandas as pd

# # response = requests.get("https://www.worldometers.info/")
# # soup = bs4.BeautifulSoup(response.text, "html.parser")

# # # Initialize lists for our specific data points
# # forest_data = []
# # co2_data = []

# # # Find all counter containers
# # for item in soup.select(".counter-group"):
# #     title = item.select_one(".counter-title").text.strip()
# #     value = item.select_one(".counter-number").text.strip()
    
# #     if "Forest Lost This Year" in title:
# #         forest_data.append(value)
# #     elif "CO2 Emissions This Year" in title:
# #         co2_data.append(value)

# # # Create DataFrame with only the columns we want
# # environmental_df = pd.DataFrame({
# #     "forest loss this year": forest_data,
# #     "carbon dioxide co2 emission": co2_data
# # })

# # print(environmental_df)
# # environmental_df.to_csv("environmental_stats.csv", index=False)

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Updated headers to prevent blocking
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
# }

# url = "https://www.worldometers.info/"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# # Initialize dictionary to store data
# data = {}

# # Find all counter sections
# for section in soup.select('div.section-counter'):
#     title = section.select_one('h2').text.strip() if section.select_one('h2') else ""
    
#     # Check if this is the Environment section
#     if "Environment" in title:  
#         for counter in section.select('div.counter-block'):
#             label = counter.select_one('div.counter-title').text.strip()
#             value = counter.select_one('span.counter-number').text.strip()
            
#             if "forest" in label.lower():
#                 data["Forest Lost This Year"] = value
#             elif "co2" in label.lower():
#                 data["CO2 Emissions This Year"] = value

# # Create and save DataFrame
# df = pd.DataFrame([data])
# print(df)
# df.to_csv("worldometers_environment.csv", index=False)