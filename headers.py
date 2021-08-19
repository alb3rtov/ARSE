######################################################################
# Program name      : headers.py 
# Author/s          : Alberto Vázquez
# Purpose           : Contains dictionaries for each website header
# Version:          : 0.1.8-alpha
######################################################################

idealista_headers = {
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

milanuncios_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64',
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}

github_headers = {
    'Referer': 'https://github.com/alb3rtov/ARSE',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
}

pisos_headers = {
    'Referer': 'https://www.pisos.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
}

vivados_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.vivados.es',
    'If-Modified-Since': 'Thu, 19 Aug 2021 12:24:04 GMT',
    'If-None-Match': 'W/"50f74e6c3469053db412583bec7158a7"',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
}

fotocasa_headers = {
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