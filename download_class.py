import sys
import re



import requests
from bs4 import BeautifulSoup


def download_story(url):
    name = re.findall('https://www.136book.com/(\w+)/',url)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) \
        Chrome/18.0.1025.166  Safari/535.19'}
    response = requests.get(url=url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    soup_texts = soup.find('div', id='book_detail', class_='box1').find_next('div')
    # open file
    filename = name + '.txt'
    f = open(filename, 'w')
    # loop analysis urls
    for link in soup_texts.ol.children:
        if link != '\n':
            print(link.text + ':' + link.a.get('href'))
            download_url = link.a.get('href')
            download_req = requests.get(download_url, headers=headers, verify=False)
            download_soup = BeautifulSoup(download_req.text, 'lxml')
            # print download_soup.get_text()
            download_soup_texts = download_soup.find('div', id='content').select("p")
            # write title
            f.write(link.text + '\n\n')
            # write chapter content
            for p in download_soup_texts:
                f.write(p.text)
                f.write('\n')
            f.write('\n\n')
    f.close()

if __name__ == '__main__':
    # download_story('https://www.136book.com/qiangweihangban/')
    download_story('https://www.136book.com/huaqiangu/')