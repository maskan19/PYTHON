import requests
from bs4 import BeautifulSoup
# anacoda때문에 따로 설치할 필요가 없다
 
response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
txt = response.text
 
# print(txt)
 
soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)