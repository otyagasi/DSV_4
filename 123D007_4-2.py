import bs4 
import requests

URL = "https://kbse.nit.ac.jp/member/"
response = requests.get(URL)
response.encoding="UTF-8"
soup = bs4.BeautifulSoup(response.text, 'html.parser')
list = soup.find_all('dl',class_="bordered")

for item in list:
    dd_tags = item.find_all('dd')
    for dd in dd_tags:
        print(dd.text)
