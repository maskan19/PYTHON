import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

 
 
 
 
driver = webdriver.Chrome('C:/Users/PC-25/Downloads/chromedriver.exe')
driver.get('http://localhost/MYSERVER/login') 
time.sleep(1)
driver.get('http://localhost/MYSERVER/secret') 
print(driver.page_source)
td = driver.find_element_by_tag_name("td")
print(td)


 #
# response = requests.get('http://localhost/MYSERVER/secret')
 #
# txt = response.text
 #
# soup = BeautifulSoup(txt, 'html.parser')
 #
# for info in soup.select('td'):
    #
    # print(info.text)