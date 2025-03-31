import requests
import bs4
import pandas as pd

response = requests.get("http://books.toscrape.com")
print(response)

#print(response.text) #this prints the text of what's coming though from the request
soup = bs4.BeautifulSoup(response.text, "html.parser")
# print(soup) #prints what was grabbed in soup variable
#print(soup.select(".mw-heading")) # this uses similar syntax to CSS - you can use "." or "#" to select classes or ids
headings = []
for item in soup.select(".page_inner"): #use h3 if you want it without the xtra text - but do this by inspecting the website to find the heading pages 
    headings.append(item.text)
    print(item.text)

heading_df = pd.DataFrame()
heading_df["headings"] = pd.Series (headings).values
print(heading_df["headings"])

#heading_df.to_csv("heading_result.csv") #if the code gets run multiple times without changing the name, it will override the old file

# look at toscrape.com to practice scraping
