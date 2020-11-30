import requests
from bs4 import BeautifulSoup
import json
import csv




class SearchEngine:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) '
                      'Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate'
    }

    headers_mail = {'Accept':
                    'text / html, application / xhtml + xml, '
                    'application / xml; q = 0.9, image / avif, '
                    'image / webp, image / apng, * / *;q = 0.8,'
                    'application / signed - exchange; v = b3; q = 0.9',
                    'Accept - Encoding': 'gzip, deflate, br',
                    'Accept - Language': 'ru - RU, ru; q = 0.9, '
                                         'en - US; q = 0.8, en; q = 0.7',
                    'Connection': 'keep - alive',
                    'User - Agent':
                    'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                    'AppleWebKit / 537.36(KHTML, like Gecko) '
                    'Chrome / 87.0.4280.66 Safari / 537.36'}

    def google_search(results_count, query):
        urls_list = []
        title_list = []
        request = requests.Session()
        query = '+'.join(query.split())
        lastpage = 0  # передаем с какой страницы должны
        # получать последние 10 результатов
        while len(urls_list) < results_count:
            url = str('https://www.google.com/search?q='
                      + query + '&' + str(lastpage)
                      + '&ie=utf-8&oe=utf-8')
            r = request.get(url, headers=SearchEngine.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            urls = soup.find_all('div', class_='yuRUbf')
            for url in urls:
                urls_list.append(url.find_all('a')[0]['href'])
                title = url.find_all('a')[0].find_all('h3')[0].span.get_text()
                title_list.append(title)
                lastpage += 10

        results = zip(title_list[0:results_count], urls_list[0:results_count])
        resulted_dict = {}
        for item in results:
            resulted_dict.update({item[0]: item[1]})
        return resulted_dict


def recursive_search(urls_counter: int, keyword, resulted_urls_dict):
    recursive_results_dict = {}
    for title, link in resulted_urls_dict.items():
        request = requests.Session()
        r = request.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        recursive_urls = soup.find_all('a')
        for url in recursive_urls:
            if str(url.get('href')).startswith('http'):
                if keyword in str(url.get_text()):
                    recursive_results_dict.update(
                        {url.get_text(): url.get('href')})
            else:
                recursive_results_dict.update({title: link})
        if len(recursive_results_dict) > urls_counter:
            break

    results = zip(list(recursive_results_dict.keys())[0:urls_counter],
                  list(recursive_results_dict.values())[0:urls_counter])
    resulted_dict = {}
    for item in results:
        resulted_dict.update({item[0]: item[1]})
    return resulted_dict


class OutputMethods:

    def json_output(self, filename, results):
        with open(filename, 'w', encoding='utf-8') as wf:
            json.dump(results, wf, ensure_ascii=False, indent=4)

    def csv_output(self, filename, results):
        with open(filename, mode="w", encoding='utf-8') as csv_wf:
            writer = csv.writer(csv_wf)
            for key, value in results.items():
                writer.writerow((key, value))
