import os
import sys
import urllib.request
client_id = "1qULcIuln9XmcjS3Sb8o" # 개발자센터에서 발급받은 Client ID 값
client_secret = "Dy466mrARq" # 개발자센터에서 발급받은 Client Secret 값
code = "0"
url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    
    
    
    import os
import sys
import urllib.request
client_id = "1qULcIuln9XmcjS3Sb8o" # 개발자센터에서 발급받은 Client ID 값
client_secret = "Dy466mrARq" # 개발자센터에서 발급받은 Client Secret 값
key = "YOUR_CAPTCHA_KEY" # 캡차 Key 값
url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    print("캡차 이미지 저장")
    response_body = response.read()
    with open('captcha.jpg', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)
    
code = "1"
key = "YOUR_CAPTCHA_KEY"
value = "YOUR_INPUT"
url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)