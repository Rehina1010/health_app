import asyncio

import aiohttp
from bs4 import BeautifulSoup

async def search_user_query(query: str) -> list[dict]:
    print("Start search user query")
    res = []
    search_url = f"https://hotline.ua/ua/sr/?q={query.replace(' ', '+')}"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            print("Status:", response.status)

            html = await response.text()
            bs = BeautifulSoup(html, "lxml")
            catalog = bs.find("div", attrs={'class':"search-list__body"})
            items = catalog.find_all("div", class_="list-item flex")
            print(type(items))
            for el in items:
                title = el.find("a", class_="item-title text-md link link--black").text.strip()
                img = f"https://hotline.ua/{el.find("img", class_="rounded-border--sm")["src"]}"
                price = el.find("div", class_="text-md text-orange text-lh--1").text.strip()
                compare = f"https://hotline.ua/{el.find("a", class_="btn btn--orange")["href"]}"
                item = {"title": title, "img": img, "price": price, "compare": compare}
                res.append(item)

    return res


if __name__ == '__main__':
    asyncio.run(search_user_query("Headphones"))