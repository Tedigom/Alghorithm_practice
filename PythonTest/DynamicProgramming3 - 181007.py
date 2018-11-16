# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
# 첫번째 시도
def solution(triangle):
    memo = {1:[0], 2:[[0,0],[0,1]]}

    def dp(N):
        if N == 1:
            return memo[1]
        elif N == 2:
            return memo[2]
        else:
            for i in range(3,N+1):
                memo[i] = []
                for j in range(len(memo[i-1])):
                    a = dp(i-1)[j].copy()
                    b = dp(i-1)[j].copy()
                    a.append(a[-1])
                    b.append(b[-1]+1)
                    memo[i].append(a)
                    memo[i].append(b)
            return memo[N]

    n = len(triangle)
    dp(n)

    answer = []
    for i in range(len(memo[n])):
        sum = 0
        for j in range(n):
            sum += triangle[j][memo[n][i][j]]
        answer.append(sum)
    return max(answer)

'''
풀이의 의도는
        0
       0 1
      0 1 2
     0 1 2 3
등으로 모든 경로를 구한후, 경로에 따른 트라이앵글 원소의 값을 대입하여
더한 값의 max를 구하려 했지만 시간초과로 풀지 못했다.

'''

# 두번째 시도
def solution(triangle):
    for i in range(len(triangle)-1,-1,-1):
        if i ==0 :
            break;
        for j in range(len(triangle[i-1])):
            if triangle[i][j] + triangle[i-1][j] >= triangle[i][j+1]+triangle[i-1][j]:
                triangle[i-1][j] = triangle[i][j] + triangle[i-1][j]
            else:
                triangle[i-1][j] = triangle[i][j+1] + triangle[i-1][j]

    answer = triangle[0][0]
    return answer

'''
dp를 이용하여 풀지는 않았지만, 아래에서 부터 올라오면서 최댓값들만
추린 결과로 맨 꼭대기 값이 최댓값이 나오도록 하였다.
'''
