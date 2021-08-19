import requests
from bs4 import BeautifulSoup 

class Milanuncios():
    def __init__(self, town, province, flat_type, max_price, min_price, num_page):
        self.zone_list = []
        self.prices_list = []
        self.url_list = []

        self.main_url = 'https://www.milanuncios.com/alquiler-de-'
        self.prices_tag = 'div aditem-price'
        self.zones_tag = 'a aditem-detail-title'

        self.milanuncios_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'
        }

        url = self.generate_url(town, province, flat_type, max_price, min_price)
        response = requests.get(url, headers=self.milanuncios_headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.generate_data_lists(soup)
    
    def generate_data_lists(self, soup):
        """ Get all data and convert into several lists """
        prices_tags_list = self.prices_tag.split()
        price_tag = prices_tags_list[0]
        price_class = prices_tags_list[1]

        zones_tags_list = self.zones_tag.split()
        zone_tag = zones_tags_list[0]
        zone_class = zones_tags_list[1]

        current_zone_list = soup.findAll(zone_tag,{'class':zone_class})
        self.zone_list = self.zone_list + current_zone_list
        self.prices_list = self.prices_list + soup.findAll(price_tag,{'class':price_class})                    
        self.url_list = self.url_list + self.generate_url_list(current_zone_list)

    def generate_url_list(self, current_zone_list):
        """ Generate url list from HTML page code """
        url_list = []

        for zone in current_zone_list:
            if zone.attrs["href"][0] == "/":
                url_list.append('https://www.milanuncios.com' + zone.attrs['href'])
            else:
                url_list.append(self.main_url + zone.attrs['href'])

        return url_list

    def generate_url(self, town, province, flat_type, max_price, min_price):
        """ Generate the main url """
        url = self.main_url + flat_type + '-en-' + town + '-' + province.replace('-','_') + '/' + '?fromSearch=1&desde=' + min_price + '&hasta=' + max_price + '&demanda=n/'
        return url

    def get_info(self):
        """ Return data to scrap selecter """
        return self.zone_list, self.prices_list, self.url_list