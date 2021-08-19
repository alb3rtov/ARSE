import requests
from bs4 import BeautifulSoup 

class Pisos():
    def __init__(self, town, province, flat_type, max_price, min_price, num_page):
        self.zone_list = []
        self.prices_list = []
        self.url_list = []

        self.main_url = 'https://www.pisos.com/alquiler/'
        self.prices_tag = 'span ad-preview__price'
        self.zones_tag = 'a ad-preview__title'

        self.pisos_headers = {
            'Referer': 'https://www.pisos.com/',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        }

        url = self.generate_url(town, flat_type, max_price, min_price)
        response = requests.get(url, headers=self.pisos_headers)
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
                url_list.append('https://www.pisos.com' + zone.attrs['href'])
            else:
                url_list.append(self.main_url + zone.attrs['href'])

        return url_list

    def generate_url(self, town, flat_type, max_price, min_price):
        """ Generate the main url """
        url = self.main_url + flat_type + "-" + town.replace("-","_") + "_capital/desde-" + min_price + "/hasta-" + max_price + "/"
        return url

    def get_info(self):
        """ Return data to scrap selecter """
        return self.zone_list, self.prices_list, self.url_list