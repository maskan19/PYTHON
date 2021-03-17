# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
client_id = "Rp05Cu_XmoiS8RXZUsSa"
client_secret = "qbHi8BLlg9"
encText = urllib.parse.quote("기아차")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    soup = BeautifulSoup(response_body, 'xml')
    for info in soup.select('item'):
        print("포스트 제목: ", info.title.text)
        print("포스트 링크: ", info.link.text)
        print("포스트 내용: ", info.description.text)
        print("작성자: ", info.bloggername.text)
        print("작성자 블로그: ", info.bloggerlink.text)
        print("작성일: ", info.postdate.text)
        print("")
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
 
# for item in soup.select('.tbody > dt > a'):
    # print(item['title'], 
          # item['href'][item['href'].find('/Stock/')+7:item['href'].find('_blank')-3])
    # print(item.find_parents('.tbody').children('dd'))
    
for info in soup.select('.tbody'):
    print(info.dt.text, end="\t\t")
    print(info.dd['id'][len(info.dd['id']) - 6:], end="\t\t")
    print(info.dd.span.text)
