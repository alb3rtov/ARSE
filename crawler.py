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

zones_tag = {"milanuncios" : "a aditem-detail-title",
            "fotocasa" : "h3 re-Card-title"
}

def main_crawler(format_address, website_list, latitude, longitude):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }

    for i in range(len(website_list)):
        website_name = urllib.parse.urlparse(website_list[i])
        website_name = website_name.netloc[4:]
        website_name = website_name[:-4]

        url = generate_url(website_list[i], format_address, website_name)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        prices_tags_list = prices_tag.get(website_name).split()
        price_tag = prices_tags_list[0]
        price_class = prices_tags_list[1]

        zones_tag_list = zones_tag.get(website_name).split()
        zone_tag = zones_tag_list[0]
        zone_class = zones_tag_list[1]

        zone_list = soup.findAll(zone_tag,{"class":zone_class})
        prices_list = soup.findAll(price_tag,{"class":price_class})

        for zone, price in zip(zone_list, prices_list):
            print(zone.get_text() + " - " + price.get_text())

def generate_url(url_website, format_address, website_name):
    if website_name == "milanuncios":
        url = url_website + format_address + "-" + format_address.replace("-","_") + "/"
        return url
    elif website_name == "fotocasa":
        #url = "https://www.fotocasa.es/es/alquiler/viviendas/"  + format_address + "-capital/todas-las-zonas/l/&gridType=3&latitude=" + latitude + "&longitude=" + longitude 
        return
    elif website_name == "idealista":
        return
    else:
        return