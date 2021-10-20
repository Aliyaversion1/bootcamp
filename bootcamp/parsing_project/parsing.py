import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

	
def main():
    notebooks_url = 'https://ultra.kg/catalog/noutbuki-planshety-i-kompyutery/noutbuki/'
    pages = '?page='
    get_html(notebooks_url)
main()