import urllib.parse
import requests
import xlsxwriter
import os
import sys
from urllib.request import Request, urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
from tkinter import messagebox

""" Global lists and dics """
def_url_sites_list = ["https://www.milanuncios.com/alquiler-de-",
                    "https://www.fotocasa.com/es/alquiler/",
                    "https://www.idealista.com/alquiler-viviendas/",
                    "https://www.pisos.com/alquiler/",
                    "https://www.vivados.com/alquilar/"
]

housing_types = ["pisos",
            "estudios",
            "apartamentos",
            "casas",
            "chalets",
            "aticos"
]

prices_tag = {"milanuncios" : "div aditem-price",
            "fotocasa" : "span re-Card-price",
            "pisos" : "span ad-preview__price",
            "vivados" : "span baseprice"
}

zones_tag = {"milanuncios" : "a aditem-detail-title",
            "fotocasa" : "h3 re-Card-title",
            "pisos" : "a ad-preview__title",
            "vivados" : "div title"
}

next_page_index = {"milanuncios" : "&pagina=",
                "fotocasa" : "/l",
                "vivados" : "?page="
}

def main_crawler(town, province, website_list, flat_type, max_price, min_price, num_page_search, xlsxfile_path, master):
    """ Request the HTML code of each listed website and extract the relevant information """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }

    num_results = 0

    # Loop for websites selected by user
    for i in range(len(website_list)):
        website_name = urllib.parse.urlparse(website_list[i])
        website_name = website_name.netloc[4:]
        website_name = website_name[:-4]
        
        url = generate_url(website_list[i], town, province, website_name, flat_type, max_price, min_price)
        first_iteration = True

        # If user select 6 o more pages set a big number for get all possible results
        if num_page_search == "6 o más":
            num_page_search = 9999

        # Loop for the num of pages selected
        for j in range(int(num_page_search)):
            if first_iteration:
                first_iteration = False
            else:
                url = generate_next_url(url, website_name, str(j+1))

            # Request and get HTML code
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Get appropriate tags for website
            prices_tags_list = prices_tag.get(website_name).split()
            price_tag = prices_tags_list[0]
            price_class = prices_tags_list[1]

            zones_tag_list = zones_tag.get(website_name).split()
            zone_tag = zones_tag_list[0]
            zone_class = zones_tag_list[1]

            # Find necesarry tags
            zone_list = soup.findAll(zone_tag,{"class":zone_class})
            prices_list = soup.findAll(price_tag,{"class":price_class})

            num_results += len(zone_list)

            for zone, price in zip(zone_list, prices_list):
                #print(zone.get_text() + " - " + price.get_text() + " - " + zone.attrs["href"])
                print(zone.get_text() + " - " + price.get_text())
    
    messagebox.showinfo("Resultados","Se han encontrado " + str(num_results) + " resultados")
    
    if num_results != 0:
        generate_xlsxfile(xlsxfile_path)
        open_xlsxfile(xlsxfile_path, master)
    else:
        generate_xlsxfile(xlsxfile_path)
        open_xlsxfile(xlsxfile_path, master)

def open_xlsxfile(xlsxfile_path, master):
    """ Ask if user want to open XLSX file """
    openfile = messagebox.askquestion("Archivo XLSX generado","Se ha generado un archivo XLSX con los resultados encontrados (" + xlsxfile_path + "). ¿Deseas abrir el archivo?")
    
    if openfile == "yes":
        master.destroy()
        os.system(xlsxfile_path)

def generate_xlsxfile(xlsxfile_path):
    """ Generate XLSX file with the results found """
    workbook = xlsxwriter.Workbook(xlsxfile_path)
    worksheet = workbook.add_worksheet()

    workbook.close()

def generate_next_url(url, website_name, page):
    """ Generate url for the next page of a given website """
    if website_name == "milanuncios":
        url = url + next_page_index.get(website_name) + page
        print(url)
        return url
    elif website_name == "fotocasa":
        return
    elif website_name == "idealista":
        return
    elif website_name == "pisos":
        url = url + page + "/"
        print(url)
        return url
    elif website_name == "vivados":
        url = url + next_page_index.get(website_name) + page
        print(url)
        return url
    else:
        return

def generate_url(url_website, town, province, website_name, flat_type, max_price, min_price):
    """ Generate the main url based on each website """
    if website_name == "milanuncios":        
        url = url_website + flat_type + "-en-" + town + "-" + province.replace("-","_") + "/" + "?fromSearch=1&desde=" + min_price + "&hasta=" + max_price + "&demanda=n/"
        print(url)
        return url

    elif website_name == "fotocasa":
        if flat_type == "pisos":
            flat_type = "viviendas"
        
        url_location = 'https://nominatim.openstreetmap.org/search/' + town +'?format=json'
        response = requests.get(url_location).json()

        url = url_website + flat_type + "/" + town + "-capital/todas-las-zonas/l?latitude=" + response[0]["lat"] + "&longitude=" + response[0]["lon"] + "&minPrice=" + min_price + "&maxPrice=" + max_price
        print(url)
        return url

    elif website_name == "idealista":
        return

    elif website_name == "pisos":
        url = url_website + flat_type + "-" + town.replace("-","_") + "_capital/desde-" + min_price + "/hasta-" + max_price + "/"
        print(url)
        return url

    elif website_name == "vivados":
        url_website = url_website.replace("com", "es")
        url = url_website + flat_type + "-desde-" + min_price + "-hasta-" + max_price + "-euros-" + town
        print(url)
        return url

    else:
        return