# https://programmers.co.kr/learn/courses/30/lessons/43104?language=python3

def solution(N):
    memo = [0]*(N+1)
    memo[1] = 1
    memo[2] = 1
    def calculateSide(N):
        if N == 1 or N == 2:
            return memo[1]
        memo[N] = calculateSide(N-1) + calculateSide(N-2)
        return memo[N]

    side = calculateSide(N)
    formerSide = memo[N-1]

    answer = 2*side+2*(side+formerSide)
    return answer

'''
What I learned

DP로 플었지만, 효율성이 잘 안나온다.
이 식이랑 차이가 그렇게 큰가?

def solution(N):
    cache = [-1 for i in range(N + 1)]
    def fibo(N):
        if N == 0:
            return 0
        if N <= 2:
            return 1
        if cache[N] != -1:
            return cache[N]
        cache[N] = fibo(N - 1) + fibo(N - 2)
        return cache[N]
    fibo(N)
    return 4*fibo(N) + 2*fibo(N - 1)

'''

'''
iterable 하게 푼 문제

def solution(N):
    l=[1,1]
    for i in range(2,N):
        l.append(l[-1]+l[-2])
    answer = (l[-1]*2+l[-2])*2
    return answer
'''
