import requests
import bs4
import csv
import pandas as pd

response = requests.get("https://energy.usgs.gov/uswtdb/data/")

soup = bs4.BeautifulSoup(response.text, "html.parser")
print(response.status_code)  # Should print 200 (success)
print(len(response.text)) 

turbines = []
for row in soup.select('table tr')[1:]:  # skips header
    cols = row.find_all('td')
    turbines.append({
        'height': cols[4].text,  # Hub height (m)
        'capacity': cols[5].text  # MW
    })

with open('turbine_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['height', 'capacity'])
    writer.writeheader()
    writer.writerows(turbines)