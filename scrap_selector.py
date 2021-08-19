######################################################################
# Program name      : scrap_selector.py 
# Author/s          : Alberto Vázquez
# Purpose           : Selects the spider for each website
# Version:          : 1.0.2-alpha
######################################################################

import os
import urllib.parse
import urllib.request
import re
import sys
import xlsxwriter

from spiders.Fotocasa import Fotocasa
from spiders.Idealista import Idealista
from spiders.Milanuncios import Milanuncios
from spiders.Pisos import Pisos
from spiders.Vivados import Vivados
from urllib.request import HTTPError
from tkinter import messagebox

""" Global lists and dics """
def_url_sites_list = ["https://www.milanuncios.com/alquiler-de-",
                    "https://www.fotocasa.com/es/alquiler/",
                    "https://www.idealista.com/buscar/alquiler-",
                    "https://www.pisos.com/alquiler/",
                    "https://www.vivados.com/alquilar/"
]

def check_internet_connection():
    """ Check internet connection """
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False

def select_spider(website_name, town, province, flat_type, max_price, min_price, num_page):
    """ Select the spider of the website """
    if website_name == "milanuncios":
        spider = Milanuncios(town, province, flat_type, max_price, min_price, num_page)
        return spider.get_info()
    elif website_name == "fotocasa":
        spider = Fotocasa(town, province, flat_type, max_price, min_price, num_page)
        return spider.get_info()
    elif website_name == "idealista":
        spider = Idealista(town, province, flat_type, max_price, min_price, num_page)
        return spider.get_info()
    elif website_name == "pisos":
        spider = Pisos(town, province, flat_type, max_price, min_price, num_page)
        return spider.get_info()
    elif website_name == "vivados":
        spider = Vivados(town, province, flat_type, max_price, min_price, num_page)
        return spider.get_info()


def open_xlsxfile(xlsxfile_path, master):
    """ Ask if user want to open XLSX file """
    openfile = messagebox.askquestion("Archivo XLSX generado","Se ha generado un archivo XLSX con los resultados encontrados (" + xlsxfile_path + "). ¿Deseas abrir el archivo?")
    
    if openfile == "yes":
        master.destroy()
        os.system(xlsxfile_path)
        sys.exit()

def generate_xlsxfile(xlsxfile_path, zone_list, prices_list, url_list):
    """ Generate XLSX file with the results found """
    workbook = xlsxwriter.Workbook(xlsxfile_path)
    worksheet = workbook.add_worksheet()

    titles = ["Zona/Calle", "Precio", "URL"]
    col = 0
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})

    # Write titles
    for title in titles:
        worksheet.write(0, col, title, bold)
        col += 1
    
    col = 0
    row = 1

    for zone, price, url in zip(zone_list, prices_list, url_list):
        data_list = [zone.get_text(), price.get_text(), url]
        clean_data_list = clean_data(data_list)

        worksheet.write(row, col, clean_data_list[0])
        worksheet.write(row, col+1, clean_data_list[1], money)
        worksheet.write(row, col+2, clean_data_list[2])
        row += 1

    workbook.close()

    return row

def clean_data(data_list):
    """ Clean data of spaces and special characters """
    clean_data_list = []
    
    for data in data_list:
        clean_line = re.sub('\s+',' ', str(data))
        clean_data_list.append(clean_line)

    return clean_data_list

def main_crawler(town, province, website_list, flat_type, max_price, min_price, num_page_search, xlsxfile_path, master):
    """ Request the HTML code of each listed website and extract the relevant information """
    if check_internet_connection():
        try:
            zone_list = []
            prices_list = []
            url_list = []

            # Loop for websites selected by user
            for i in range(len(website_list)):
                website_name = urllib.parse.urlparse(website_list[i])
                website_name = website_name.netloc[4:]
                website_name = website_name[:-4]

                # If user select 6 o more pages set a big number for get all possible results
                if num_page_search == "6 o más":
                    num_page_search = 9999 # FIX THIS

                for j in range(int(num_page_search)):
                    aux_zone_list, aux_prices_list, aux_url_list = select_spider(website_name, town, province, flat_type, max_price, min_price, j)
                    zone_list = zone_list + aux_zone_list
                    prices_list = prices_list + aux_prices_list
                    url_list = url_list + aux_url_list

                    aux_zone_list.clear()
                    aux_prices_list.clear()
                    aux_url_list.clear()

            #for zone, price, url in zip(zone_list, prices_list, url_list):
            #    print(zone.get_text() + " - " + price.get_text() + " - " + url)
            
            # Check if results have been found
            if len(zone_list) != 0:
                messagebox.showinfo("Resultados","Se han encontrado " + str(len(zone_list)) + " resultados")
                generate_xlsxfile(xlsxfile_path, zone_list, prices_list, url_list)
                open_xlsxfile(xlsxfile_path, master)
            else:
                messagebox.showinfo("Resultados","Se han encontrado " + str(len(zone_list)) + " resultados.\nNo se generará ningún archivo XLSX.")

        except HTTPError as e:
            messagebox.showerror("HTTPError",e)
        except AttributeError as e:
            messagebox.showerror("AttributeError",e)
    
    else:
        messagebox.showwarning("Error en la conexión a internet", "Error conectando con los servidores.\nComprueba tu conexión a Internet.")

"""def generate_next_url(url, website_name, page):

    if website_name == "milanuncios":
        url = url + next_page_index.get(website_name) + page
        #print(url)
        return url
    elif website_name == "fotocasa":
        return
    elif website_name == "idealista":
        url = url + next_page_index.get(website_name) + page + ".htm"
    elif website_name == "pisos":
        url = url + page + "/"
        #print(url)
        return url
    elif website_name == "vivados":
        url = url + next_page_index.get(website_name) + page
        #print(url)
        return url
    else:
        return"""