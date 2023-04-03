import requests
from bs4 import BeautifulSoup

URL = "https://intermedia.kg/catalog/noutbuki-i-aksessuary/noutbuki-i-ultrabuki/"

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
        'div', class_="item product sku"
    )
    laptops = []
    for item in items:
        laptop = {
            "description": item.find('div', class_="productColText").find('span', class_='middle').string,
            "link": item.find('div', class_="productColText").find('a').get("href"),
            "price": item.find('div', class_="productColText").find('a', class_='price').string
        }
        laptops.append(laptop)
    return laptops


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        laptops = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data_from_page(html.text)
            laptops.extend(current_page)
        return laptops
    else:
        raise Exception("Error in parser")
