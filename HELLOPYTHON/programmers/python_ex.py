numbers = [5,0,2,7]

def solution(numbers):
    answer = []
    for i in len(numbers):
        for j in len(numbers)-i:
            answer.append(numbers[i]+numbers[j])
    print(answer)
    return answer



def BubbleSort(li):
    list_length = len(li)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]