import requests

def get_locations(url, key_index, value_index):
    """ Use geoapi to get all locations of Spain in a option menu """
    response = requests.get(url).json()

    value_list = []
    key_list = []

    for ccaa in response["data"]:
        key_list.append(ccaa[key_index])
        value_list.append(ccaa[value_index])

    return key_list, value_list