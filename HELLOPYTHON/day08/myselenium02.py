from selenium import webdriver

driver = webdriver.Chrome('C:/Users/PC-25/Downloads/chromedriver.exe')
driver.get('http://localhost/MYSERVER/login.html') 
driver.find_element_by_id('u_name').send_keys('abe')
driver.find_element_by_id('pwd').send_keys('1')
driver.find_element_by_id('mysubmit').click()
driver.implicitly_wait(3)
driver.get('http://localhost/MYSERVER/secret') 

td = driver.find_elements_by_tag_name("td")
for name in td:
    print(name.text)
