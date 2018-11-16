# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    answer = []
    while len(prices)>0:
        cnt = 0
        for i in range(len(prices)):
            if prices[0]>prices[i]:
                answer.append(cnt)
                break;
            elif i == len(prices)-1:
                answer.append(cnt)
                break;
            cnt += 1
        prices.pop(0)
    return answer

'''
what I learned

1. 내가 짠 코드는 효율성이 안나왔다.
아래 다른 코드를 참조하여 효율성이 나은 코드를 소개한다.
'''
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

'''
비슷한 느낌이긴 하지만 큐를 사용하고,
c를 popleft 함으로써 과정을 한번 줄이는듯 하다.
'''
