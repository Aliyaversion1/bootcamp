import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    responce = requests.get(url)
    return responce.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_="catalog-list")
    cars = catalog.find_all('a', class_= 'catalog-list-item')
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = 'A car'
        
        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = 'https://motoring.pxcrush.net/motoring/general/editorial/mazda-rx-vision_gt3_concept-2020-05.jpg?height=580&width=1021&aspect=centered'
        
        try:
            price = car.find('span', class_='catalog-item-price').text.strip()
        except:
            price = 'Договорная'

        data = {
            'title': title,
            'price': price,
            'img': img
        }
        write_to_csv(data)
def write_headers():
    with open('cars.csv', 'a') as file:
        fieldnames = ["Марка","Цена","Фото"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        fieldnames = ["Марка","Цена","Фото"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"Марка": data['title'],"Цена": data['price'],"Фото":data['img']})
def main():
    with open('cars.csv', 'w') as file:pass
    write_headers()
    i = 1
    while True:
        cars_url = f'https://cars.kg/offers/{i}?vendor=57fa24ee2860c45a2a2c0905'
        html = get_html(cars_url)
        catalog = BS(html, 'lxml').find('div', class_="catalog-list")
        if not catalog:
            break
        get_data(html)
        i += 1

        


main()