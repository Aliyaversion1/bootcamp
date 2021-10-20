import requests
from bs4 import BeautifulSoup as BS
import csv
def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BS(html,'lxml')
    pages_ul = soup.find('div',class_ = 'bx-pagination-container row').find('ul')
    last_page = pages_ul.find_all('li')[-2]
    total_page = last_page.find('a').get('href').split('=')[-1]
    return int(total_page)

def get_page_data(html):
    soup = BS(html, 'lxml')
    product_list = soup.find('div', 'class_="item product sku"')


def main():
    notebooks_url = 'https://ultra.kg/catalog/noutbuki-planshety-i-kompyutery/noutbuki/'
    pages = '1='
    get_total_pages(get_html(notebooks_url))

main()