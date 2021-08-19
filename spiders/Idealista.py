import requests
from bs4 import BeautifulSoup 

class Idealista():
    def __init__(self, town, province, flat_type, max_price, min_price, num_page):
        self.zone_list = []
        self.prices_list = []
        self.url_list = []

        self.main_url = 'https://www.idealista.com/buscar/alquiler-'
        self.prices_tag = 'span item-price h2-simulated'
        self.zones_tag = 'a item-link'
        
        self.idealista_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'didomi_token=eyJ1c2VyX2lkIjoiMTdhNjg2MGMtZjU1Ni02ZWIwLWJlZjQtNzYxMGU0ZjhlMjBjIiwiY3JlYXRlZCI6IjIwMjEtMDctMDJUMTg6MDA6MzMuMjE3WiIsInVwZGF0ZWQiOiIyMDIxLTA3LTAyVDE4OjAwOjMzLjIxN1oiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnMiOnsiZW5hYmxlZCI6WyJnb29nbGUiLCJmYWNlYm9vayIsImM6bWl4cGFuZWwiLCJjOmFidGFzdHktTExrRUNDajgiLCJjOmhvdGphciIsImM6eWFuZGV4bWV0cmljcyIsImM6YmVhbWVyLUg3dHI3SGl4IiwiYzp0ZWFsaXVtY28tRFZEQ2Q4WlAiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIl19fQ==; euconsent-v2=CPIuUqMPIuUqMAHABBENBfCoAP_AAAAAAAAAF5wBAAIAAtAC2AvMAAABAaBSAFYALgAhgBkADLAGoANkAdgA_ACAAEFAIwAUsAp4BV4C0ALSAawA3gB1QD5AIbAQ6AioBF4CRAE2AJ2AUiAuQBgQDCQGHgMYAZOAzkBngDPgHJAOUAdYA_AlA-AAQAAsACgAGQAOAAigBgAGIAPAAiABMACqAFwAL4AYgAzABtAEIAIaARABEgCOAFGAKUAW4AwgBlADVAGyAO8AfgBGACOAFPAKvAWgBaQC6gGKANwAdQA-QCHQEVAIvASIAmwBYoC2AF2gLzAYeAyIBk4DLAGcgM8AZ8A0gBrADgAHWAO1Ae0A_ApBVAAXABQAFQAMgAcgA-AEAAIoAYABlADQANQAeQBDAEUAJgATwApABVACwAFwAL4AYgAzABzAEIAIaARABEgCjAFKALEAW4AwgBlADRAGqANkAd8A-wD9AIsARgAjgBKQCggFDAKuAVsAuYBeQDFAG0ANwAegBDoCLwEiAJOATYAnYBQ4CtgFigLQAWwAuABcgC7QF5gMNAYeAxgBkQDJAGTgMuAZyAzwBn0DSANJgawBrIDYwG6wOTA5QBy4DrAHagPHAe0A-UB-BCCIAAsACgAGQARAAuABiAEMAJgAVQAuABfADEAGYAN4AegBHACxAGEAMoAagA3wB3wD7APwAf4BGACOAEpAKCAUMAp4BV4C0ALSAXMAvwBigDaAHUAPQAkEBIgCTgEqAJsAU0AsUBaMC2ALaAXAAuQBdoDDwGJAMiAZOAzkBngDPgGiANJAaWA1UBwADkgHRgOsAdqA8cB-A6DuAAuACgAKgAZAA5AB8AIAARAAugBgAGUANAA1AB4AD6AIYAigBMACfAFUAVgAsQBcAF0AL4AYgAzABvADmAHoAQgAhoBEAESAI6ASwBMACaAFGAKUAWIAt4BhAGGAMgAZQA0QBqADZAG-AO8Ae0A-wD9AH-AQOAiwCMAEcgJSAlQBQQCngFXALFAWgBaQC5gF1ALyAX4AxQBtADcAHEgOmA6gB6AENgIdAREAioBF4CQQEiAJUATIAmwBOwChwFNAKsAWKAtCBbAFsgLgAXIAu0Bd4C8wGDAMJAYaAw8BiQDGAGPAMkAZOAyoBlgDLgGcgM-AaJA0gDSQGlgNOAaqA1gBsYDdQHFwOSA5UBy4DowHWAPHAekA9UB7QD5QH1wPwA_EJBgAAQAAuACgAKgAZAA5AB4AIAARAAwABlADQANQAeQBDAEUAJgAT4AqgCsAFgALgAbwA5gB6AEIAIaARABEgCOgEsAS4AmgBSgC3AGGAMgAZcA1ADVAGyAO8AewA-IB9gH6AQAAgcBFwEYAI0ARwAlIBQQClgFPAKuAXMAvwBigDWAG0ANwAbwA4gB6AD5AIbAQ6Ai8BIgCYgEygJsATsAocBSICmgFigLQAWwAuQBd4C8wGBAMGAYSAw0Bh4DIgGSAMnAZcAzkBnwDSAGnQNYA1kBusDkQOVAcuA6MB1gDxwHtAPlGQHwAKABDACYAFwARwAywBqADsgH2AfgBGACOAFLAKuAVsA3gCTgExAJsAWiAtgBeYDAgGHgMiAZyAzwBnwDkgHKAPiAfgKgQAAUACGAEwALgAjgBlgDUAHYAPwAjABHAClgFXgLQAtIBvAEggJiATYApsBbAC5AF5gMCAYeAyIBnIDPAGfANyAckA5QB-AAA.f_gAAAAAAAAA; utag_main=v_id:017a6d0c00a2000109d2f5b4315703083005207b00bd0$_sn:1$_se:1$_ss:1$_st:1625328941028$ses_id:1625327141028%3Bexp-session$_pn:1%3Bexp-session; userUUID=eefee420-c231-4ac1-93de-360104992cf4; SESSION=19bbb2924b6aefba~d87cd793-6d5c-40a0-be51-b7acee537003; cookieSearch-1="/alquiler-viviendas/ciudad-real-ciudad-real/:1629370303285"; contactd87cd793-6d5c-40a0-be51-b7acee537003="{\'email\':null,\'phone\':null,\'phonePrefix\':null,\'friendEmails\':null,\'name\':null,\'message\':null,\'message2Friends\':null,\'maxNumberContactsAllow\':10,\'defaultMessage\':true}"; datadome=GBI7faZweFMwXAFM4d4mErPleS3cpbA7vjp0_GsLbvEPoNmJMFaiNDUoHonUs1XvCh9fn0MH0WWnX0Co8Q-BbZ0Gv7Vu7RmzkdMyx~C7OS',
            'referer': 'https://www.idealista.com/',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        }

        url = self.generate_url(town, province, flat_type, max_price, min_price)
        response = requests.get(url, headers=self.idealista_headers)
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
                url_list.append('https://www.idealista.com' + zone.attrs['href'])
            else:
                url_list.append(self.main_url + zone.attrs['href'])

        return url_list

    def generate_url(self, town, province, flat_type, max_price, min_price):
        """ Generate the main url """
        if flat_type == "pisos":
            flat_type = "viviendas"
        
        url = self.main_url + flat_type + "/" + province + "-" + town + "/"
        return url

    def get_info(self):
        """ Return data to scrap selecter """
        return self.zone_list, self.prices_list, self.url_list