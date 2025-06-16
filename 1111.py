#!/usr/bin/env python3
"""
KBSE What's New 画像 URL 一覧 (関数なし超シンプル版)
---------------------------------------------------
https://kbse.nit.ac.jp/whatsnew/ の新着情報をクロールし、
各記事に含まれる <img src="…"> の画像 URL を 5 秒間隔で収集、
重複除去して昇順に表示するだけのワンショットスクリプト。
"""

import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ROOT_URL = "https://kbse.nit.ac.jp/whatsnew/"


# 1) 新着ページを取得し記事リンク収集
root_html = requests.get(ROOT_URL).text
soup = BeautifulSoup(root_html, "html.parser")

entry_links = {
    urljoin(ROOT_URL, a["href"].strip())
    for dl in soup.find_all("dl", id="news_list_dl", class_="bordered")
    for a in dl.select("dd > a[href]")
}

img_urls: set[str] = set()
entry_links = sorted(entry_links)

for idx, link in enumerate(entry_links):
    page_html = requests.get(link).text
    page_soup = BeautifulSoup(page_html, "html.parser")

    for img in page_soup.find_all("img", src=True):
        src = img["src"].strip()
        if src and not src.startswith("data:"):
            img_urls.add(urljoin(link, src))
    time.sleep(5)

# 3) 画像 URL を昇順で出力
for url in sorted(img_urls, key=lambda u: urlparse(u).path):
    print(url)
