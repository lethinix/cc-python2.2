import requests
from bs4 import BeautifulSoup
import csv

# url = "https://energy.usgs.gov/uswtdb/data/"
url = "https://energy.usgs.gov/uswtdb/viewer/#3.15/37.25/-96.25"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Crash if request failed
    
    soup = BeautifulSoup(response.text, "html.parser")
    turbines = []
    
    # Updated selector (check DevTools to confirm)
    table = soup.find("table", {"class": "data-table"})  # Adjust class name!
    if table:
        rows = table.find_all("tr")[1:]  # Skip header
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 6:  # Ensure enough columns
                turbines.append({
                    'height': cols[4].get_text(strip=True),
                    'capacity': cols[5].get_text(strip=True)
                })
    
    # Save to CSV
    with open('turbine_data.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['height', 'capacity'])
        writer.writeheader()
        writer.writerows(turbines)
    
    print(f"✅ Success! Saved {len(turbines)} turbines to turbine_data.csv")

except Exception as e:
    print(f"❌ Error: {e}")