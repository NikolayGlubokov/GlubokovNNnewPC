import requests
from bs4 import BeautifulSoup
import csv
import re


def variant_one():
    def get_html(url):
        s = requests.get(url)
        s.encoding = 'utf-8'
        return s.text

    def refined(s):
        res = re.sub(r'\D+', '', s)
        return res

    def text_refined(s):
        res = re.sub(r'\u200b?\xb2?', '', s)
        return res

    def main():
        for i in range(1,20):
            urs = f'https://www.sportmaster.ru/catalog/muzhskaya_obuv/vsya_muzhskaya_obuv/?page={i}'
            get_page_data(get_html(urs))

    def write_csv(data):
        with open('homeworkparsing2.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\r', delimiter=';')
            writer.writerow((data['name'],data['old_price'],data['new_price'],data['rating'], data['sell']))

    def get_page_data(html):
        soup = BeautifulSoup(html, 'lxml')
        elements = soup.find_all('div', class_="sm-product-card")

        for el in elements:

            try:
                new_price = refined(el.find('span', class_='sm-amount_default').text)
                print(new_price)
            except ValueError:
                new_price = ''

            try:
                name = text_refined(el.find('div', class_='sm-text').find('a').text.strip())
                print(name)
            except ValueError:
                name = ''

            try:
                if el.find('span', class_='sm-amount_old'):
                    old_price = refined(el.find('span', class_='sm-amount_old').text.strip())
                else:
                    old_price=''
                print(old_price)
            except ValueError:
                old_price = ''

            try:
                if el.find('span', class_='sm-text-text-12'):
                    rating = refined(el.find('span', class_='sm-text-text-12').text.strip())
                else:
                    rating = ''
                print(rating)
            except ValueError:
                rating = ''

            try:
                if int(old_price):
                    d = int(new_price)
                    c= int(old_price)
                    sell = round(((c-d)/c)*100,0)
                print(sell)
            except ValueError:
                sell = 'Ещё нет скидки'


            data = {
                'new_price': new_price,
                'name': name,
                'old_price': old_price,
                'rating': rating,
                'sell':sell
            }
            write_csv(data)

    if __name__ == '__main__':
        main()



variant_one()
