import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Ada_Lovelace")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")

images = soup.select('img')
# print(images)

image_links = []
for img in images:
    src = img.get("src")
    print(src)
    # image_links.append("https:" + src)
    image_links.append(f"https:{src}") #this is the same as the line above
    # print(f"https:{src}")

    import urllib.request #to download 
import urllib.parse # to download 
from urllib.error import HTTPError # to see error 

for index, url in enumerate(figure_image_links):
    file_name = 'img_' + str(index) + '.jpg'
    file_path = 'images/'    
    full_path = '{}{}'.format(file_path, file_name)
    print(file_name)
    try:
        urllib.request.urlretrieve(url, full_path)
        pass
    except urllib.error.HTTPError as err:
        print(err.code)
        pass