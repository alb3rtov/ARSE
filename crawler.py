import urllib.parse
import requests
from urllib.request import Request, urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def_url_sites_list = ["https://www.milanuncios.com/alquiler-de-estudios-en-",
                    "https://www.fotocasa.es/es/alquiler/viviendas/",
                    "https://www.idealista.com/alquiler-viviendas/ciudad-real-ciudad-real/"
]

prices_tag = {"milanuncios" : "div aditem-price",
            "fotocasa" : "span re-Card-price" 
}

def main_crawler(format_address, website_list, latitude, longitude):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }

    #url = "https://www.fotocasa.es/es/alquiler/viviendas/"  + format_address + "-capital/todas-las-zonas/l/&gridType=3&latitude=" + latitude + "&longitude=" + longitude
    url = "https://www.milanuncios.com/alquiler-de-estudios-en-" + format_address + "-" + format_address.replace("-","_") + "/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    #prices_list = soup.findAll("span",{"class":"re-Card-price"})
    #streets_list = soup.findAll("h3",{"class":"re-Card-title"})
    zone_list = soup.findAll("a",{"class":"aditem-detail-title"})
    prices_list = soup.findAll("div",{"class":"aditem-price"})

    for zone, price in zip(zone_list, prices_list):
        print(zone.get_text() + " - " + price.get_text())

    #for prices in prices_list:
    #    print(prices.get_text())
    
    print(url)
