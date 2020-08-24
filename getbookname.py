

import requests
from download_class import download_story
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'http://www.136book.com/wanjie.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) \
            Chrome/18.0.1025.166  Safari/535.19'}
    response = requests.get(url=url,headers=headers,verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    soup_texts = soup.find_all('a',target="_blank")
    for i in soup_texts:
        # print(i.text)
        url = i.get('href') #get the urls
        print(url)
        # download_story(url)
