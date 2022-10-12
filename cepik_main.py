import json

import requests
from ratelimit import limits

@limits(calls=10, period=60)
def get_json_response(url):

    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

    json_response = (requests.get(url)).json()

    return json_response


def get_car_info(url):
    api_response = get_json_response(url)
    print(api_response['data'][0]['attributes'].keys())
    print(len(api_response['data']))

car_url = 'https://api.cepik.gov.pl/pojazdy?wojewodztwo=30&data-od=20191230&data-do=20191231'

# get_car_info(car_url)

def get_url_to_file(url, wojewodztwo):
    api_response = get_json_response(url)
    print(api_response['data'][0]['attributes'].keys())
    print(api_response['data'][wojewodztwo]['attributes']['opis-zawartosci'])
    url = api_response['data'][wojewodztwo]['attributes']['url-do-pliku']
    return url


def get_file_info(url, wojewodztwo):

    api_response = get_json_response(url)
    dict = api_response['data'][wojewodztwo]['attributes']

    for key in dict:
        print(key, ' : ', dict[key])


wojewodztwo = 14 # wielkopolskie - kod

files_url = 'https://api.cepik.gov.pl/pliki'

get_file_info(files_url, wojewodztwo)