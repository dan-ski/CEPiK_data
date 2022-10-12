import requests
from ratelimit import limits

@limits(calls=10, period=60)
def connect_to_api(url):
    response = requests.get(url)
    response_code = response.status_code

    return response_code

url = 'https://api.cepik.gov.pl/pojazdy?wojewodztwo=30&data-od=20191230&data-do=20191231'
url_2 = 'https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20180101'
print(connect_to_api(url))