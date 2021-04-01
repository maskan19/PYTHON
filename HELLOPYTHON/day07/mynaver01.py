# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import re
client_id = "Rp05Cu_XmoiS8RXZUsSa"
client_secret = "qbHi8BLlg9"
encText = urllib.parse.quote("기아차")
url = "https://openapi.naver.com/v1/search/blog.xml?display=100&sort=date&query=" + encText  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read().decode('utf-8')
    soup = BeautifulSoup(response_body, 'xml')
    for item in soup.select('item'):
        print("포스트 제목: ", item.title.text)
        print("포스트 링크: ", item.link.text)
        print("포스트 내용: ", re.sub('<.+?>', '', item.description.text, 0, re.I|re.S))
        print("작성자: ", item.bloggername.text)
        print("작성자 블로그: ", item.bloggerlink.text)
        print("작성일: ", item.postdate.text)
        print("")
else:
    print("Error Code:" + rescode)
 