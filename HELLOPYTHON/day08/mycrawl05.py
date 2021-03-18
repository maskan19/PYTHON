import requests
from bs4 import BeautifulSoup
# anacoda때문에 따로 설치할 필요가 없다
 
response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
txt = response.text
 
# print(txt)
 
soup = BeautifulSoup(txt, 'html.parser')
 
# for item in soup.select('.tbody > dt > a'):
    # print(item['title'], 
          # item['href'][item['href'].find('/Stock/')+7:item['href'].find('_blank')-3])
    # print(item.find_parents('.tbody').children('dd'))
    
    
for info in soup.select('.tbody'):
    print(info.dt.text, end="\t\t")
    print(info.dd['id'][len(info.dd['id'])-6:], end="\t\t")
    print(info.dd.span.text)