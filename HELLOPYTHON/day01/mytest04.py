# input("시작 수를 넣으세요") 단, 작은 수
# input("끝 수를 넣으세요") 단, 큰 수
# 시작 수(a)에서 끝 수(b)의 합을 구하세요
a = input("시작 수를 넣으세요")     
b = input("끝 수를 넣으세요")
sum=0
for i in range(int(a), int(b)+1):
        sum+=i
print(sum)