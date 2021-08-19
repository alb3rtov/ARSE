import requests
from bs4 import BeautifulSoup 

class FotoCasa():
    def __init__(self, town, province, flat_type, max_price, min_price, num_page):
        self.zone_list = []
        self.prices_list = []
        self.url_list = []

        self.main_url = 'https://www.fotocasa.com/es/alquiler/'
        self.prices_tag = 'span re-Card-price'
        self.zones_tag = 'h3 re-Card-title'

        self.fotocasa_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'ajs_anonymous_id=%22519fce82-1e32-433a-9f9d-d5cdd050d285%22; cu=es-es; borosTcf=eyJwb2xpY3lWZXJzaW9uIjoyLCJjbXBWZXJzaW9uIjozMiwicHVycG9zZSI6eyJjb25zZW50cyI6eyIxIjp0cnVlLCIyIjp0cnVlLCIzIjp0cnVlLCI0Ijp0cnVlLCI1Ijp0cnVlLCI2Ijp0cnVlLCI3Ijp0cnVlLCI4Ijp0cnVlLCI5Ijp0cnVlLCIxMCI6dHJ1ZX19LCJzcGVjaWFsRmVhdHVyZXMiOnsiMSI6dHJ1ZX0sInZlbmRvciI6eyJjb25zZW50cyI6eyI1NjUiOnRydWV9fX0=; ASP.NET_SessionId=pzqmtonb0w1skm4gwug1w2jg; auth=pzqmtonb0w1skm4gwug1w2jg; euconsent-v2=CPK_ophPK_ophCBAgAESBnCoAP_AAP_AAAiQILtf_X__bX9n-_79__t0eY1f9_r_v-Qzjhfdt-8F2L_W_L0X_2E7NF36pq4KuR4ku3bBIQNtHMnUTUmxaolVrzPsak2Mr6NKJ7LkmnsZe2dYGHtPn91T-ZKZ7_7___f73z___9___9_3____________-_____9____________9____-CC7X_1__21_Z_v-_f_7dHmNX_f6_7_kM44X3bfvBdi_1vy9F_9hOzRd-qauCrkeJLt2wSEDbRzJ1E1JsWqJVa8z7GpNjK-jSiey5Jp7GXtnWBh7T5_dU_mSme_-___3-98____f___f9_____________v_____f____________f____gAAA; _pbjs_userid_consent_data=2922871783517005; usunico=18/08/2021:13-18610046; re_uuid=FR-gt5SutJLeRJ6DHOKqk; utag_main=v_id:017a1eedda9600160654407b722303083008507b00bd0$_sn:18$_se:1$_ss:1$_st:1629381429001$ses_id:1629379629001%3Bexp-session$_pn:1%3Bexp-session; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; AMCV_05FF6243578784B37F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18858%7CMCMID%7C24776712387536594592018860474209081115%7CMCAID%7CNONE%7CMCOPTOUT-1629386829s%7CNONE%7CvVersion%7C4.6.0; gig_canary=false; gig_canary_ver=12403-3-27156300',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        }


    def generate_url(self, town, flat_type, max_price, min_price):
        if flat_type == "pisos":
            flat_type = "viviendas"
        
        # Get latitute and longitude of the town
        url_location = 'https://nominatim.openstreetmap.org/search/' + town +'?format=json'
        response = requests.get(url_location).json()

        url = self.main_url  + flat_type + "/" + town + "-capital/todas-las-zonas/l?latitude=" + response[0]["lat"] + "&longitude=" + response[0]["lon"] + "&minPrice=" + min_price + "&maxPrice=" + max_price
        return url