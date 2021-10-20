import requests
from bs4 import BeautifulSoup as BS
import lxml

def get_html():
    response = requests.get('https://vesti.kg/').text
    return response

def get_title():
    soup = BS(get_html(), lxml)
    titles = soup.find('div', class_="itemBody")
    link_list = []
    for i in titles:
        link = i.find('h2').get('a').text
        link_list.append(link)
    print(link_list)

get_title()
def page():
    soup = BS("html", lxml)
    pages = soup.find('nav', class_='pagination')
    for i in pages:
        page = i.find('ul')

def write_to_csv():
    with open('pars', 'a') as file:
        file.write

def main():
    url_a = 'https://vesti.kg/'
    get_html(url_a)
    get_title()
    write_to_csv()

main()