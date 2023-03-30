from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/animation/?filter=popular"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response



def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(
        'div', class_="b-content__inline_item-cover"
    )
    animes = []
    for item in items:
        link_div = item.find('div', class_="b-content__inline_item-link")
        if link_div:
            info_div = link_div.find('div')
            info = info_div.getText().split(", ")
            anime = {
                "title": link_div.find('a').getText(),
                "year": info[0],
                "country": info[1],
                "genre": info[2],
                "link": link_div.find('a').get("href")
            }
            animes.append(anime)
    return animes


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animes = []
        for i in range(1, 3):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data_from_page(html.text)
            animes.extend(current_page)
        return animes
    else:
        raise Exception("Error in parser")
