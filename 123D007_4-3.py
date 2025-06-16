import bs4, requests, time, re
from urllib.parse import urljoin, urlparse

BASE = "https://kbse.nit.ac.jp/whatsnew/"
soup = bs4.BeautifulSoup(requests.get(BASE).text, "html.parser")

for a in soup.select('dl#news_list_dl.bordered dd a[href]'):
    url = urljoin(BASE, a["href"])
    time.sleep(5)                                # ★最低 5 秒★

    page = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    for img in page.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        full = urljoin(url, src)
        # --- GIF・SVG を除外する ---
        ext = re.sub(r'\?.*$', '', urlparse(full).path).lower()
        if ext.endswith((".gif", ".svg")):
            continue

        print(full)
