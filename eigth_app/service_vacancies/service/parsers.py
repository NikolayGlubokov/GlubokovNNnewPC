import requests
from bs4 import BeautifulSoup

#url = 'https://hh.ru/search/vacancy?text=python&from=suggest_post&area=1'
url='https://russia.superjob.ru/vacancy/search/?keywords=Python'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


# def hh(url):
#     resp = requests.get(url, headers=headers)
#
#     jobs = []
#     errors = []
#     if resp.status_code == 200:
#         soup = BeautifulSoup(resp.content, 'html.parser')
#         main_div = soup.find('div', class_='vacancy-serp-content')
#         if main_div:
#             div_lst = main_div.find_all('div', class_='serp-item')
#             for div in div_lst:
#                 title = div.find('h3').text
#                 href = div.find('h3').a['href']
#                 content = div.find_all('div', class_='vacancy-serp-item__info')
#                 if len(content) > 1:
#                     content = content[1].text
#                 else:
#                     content = 'Нет описания'
#
#                 comp = div.find('div', class_='vacancy-serp-item__meta-info-company').find('a')
#                 if comp:
#                     company = comp.text
#                 else:
#                     company = 'Компания неизвестна'
#
#                 jobs.append({'title': title, 'url': href, 'description': content, 'company': company})
#
#         else:
#             errors.append({'url': url, 'title': 'Разметка была изменена'})
#     else:
#         errors.append({'url': url, 'title': 'Страница не отвечает'})
#     return jobs, errors

def superjob(url):
    resp = requests.get(url, headers=headers)

    jobs = []
    errors = []
    domain = 'https://russia.superjob.ru'
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='_3VMkc')
        if main_div:
            div_lst = main_div.find_all('div', class_='f-test-search-result-item')
            for div in div_lst:
                tit = div.find('div', class_='_2J-3z')
                if tit:
                    title = tit.find('a').text
                    href = tit.find('a').get('href')
                con = div.find('div', class_='_2d_Of')
                if con:
                    content = con.find('div', class_='_3gyJS').text
                comp = div.find('span', class_='_3nMqD f-test-text-vacancy-item-company-name _2FkKs _249GZ _1jb_5 _1dIgi _3qTky')
                if comp:
                    company = comp.text



                    print(company)
#               jobs.append({'title': title, 'url': domain+href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Разметка была изменена'})
    else:
        errors.append({'url': url, 'title': 'Страница не отвечает'})

#
if __name__ == '__main__':
    jobs = superjob(url)
    h = open('work.json', 'w', encoding='utf-8')
    h.write(str(jobs))
    h.close()
