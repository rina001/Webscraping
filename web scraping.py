import bs4 as bs
import urllib.request

sauce= urllib.request.urlopen('https://baidu.com/').read()
soup= bs.BeautifulSoup(sauce,'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph)
    


