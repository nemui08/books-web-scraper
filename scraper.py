import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

book = []

for page in range(1,51):
    time.sleep(1)

    print(f"Scraping page {page}...")

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        title = item.h3.a["title"]

        price = item.find("p", class_="price_color").text
        price = float(re.sub(r"[^\d.]", "", price))

        book.append({
            "title": title,
            "price": price
        })

df = pd.DataFrame(book)

print("\nTotal book: ",len(df))

df.to_excel("books_1000.xlsx", index=False)