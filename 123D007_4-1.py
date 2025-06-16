from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
h2_tags = soup.find_all('h2')

for h2 in h2_tags:
    print(h2.text.strip())