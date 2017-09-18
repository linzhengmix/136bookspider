

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.136book.com/qiangweihangban/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = urllib2.Request(url, headers = head)
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    # open file
    f = open('../qiangweihangban.txt','w')
    # loop analysis urls
    for link in soup_texts.ol.children:
        if link != '\n':
            print(link.text+':'+link.a.get('href'))
            download_url = link.a.get('href')
            download_req = urllib2.Request(download_url, headers = head)
            download_response = urllib2.urlopen(download_req)
            download_html = download_response.read()
            download_soup = BeautifulSoup(download_html, 'lxml')
            #print download_soup.get_text()
            download_soup_texts = download_soup.find('div', id = 'content').select("p")
            # write title
            f.write(link.text + '\n\n')
            # write chapter content
            for p in download_soup_texts:
                f.write(p.text)
                f.write('\n')
            f.write('\n\n')
    f.close()