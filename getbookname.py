

import requests
from download_class import download_story
from bs4 import BeautifulSoup


def getbookurl(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) \
            Chrome/18.0.1025.166  Safari/535.19'}
    response = requests.get(url=url,headers=headers,verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    soup_texts = soup.find_all('a',target="_blank")
    urls = []
    for i in soup_texts:
        url = i.get('href')
        urls.append(url)
        print(url)
    return urls

if __name__ == '__main__':
    url = 'http://www.136book.com/wanjie.php'
    getbookurl(url=url)