# 가위바위보 게임
import random

rsp = ["가위", "바위", "보"]
com = random.randint(0, 2)
user = input("가위 바위 보!")

print("com : ",rsp[com], " user : ", user)
if user == rsp[com]:
        print("비겼습니다.")
elif (rsp.index(user)-com==1 or rsp.index(user)-com==-2):
        print("이겼습니다.")
else:
        print("졌습니다.")
