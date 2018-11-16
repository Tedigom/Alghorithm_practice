# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3#

def solution(m, n, puddles):
    grid = [[0]*(m+1) for i in  range(n+1)]
    if puddles != [[]]:
        for i in range(len(puddles)):
            grid[puddles[i][1]][puddles[i][0]] = -1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i ==1 and j == 1:
                grid[i][j] = 1
                continue
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
            grid[i][j] = (grid[i-1][j] + grid[i][j-1])%1000000007

    return grid[n][m]
'''
n,m을 헷갈리지 않고 하는것이 중요.
grid를 만들때는 grid = [[0]*(m+1) for i in range(n+1)] 으로 표현

처음 puddle를 -1로 표현했다가, iterate 들어갈 때 0으로 바꾼후, 영향을 주지 않게함.
'''
'''
처음에 했던 틀린답안 --> 이렇게 하면 안된다.
'''
def solution(m, n, puddles):
    mnlist = {}
    for i in range(1,m+1):
        for j in range(1,n+1):
            mnlist[i,j] = 0
    mnlist[m,n] = 0
    for i in range(1,m):
        mnlist[i,n] = 1
    for i in range(1,n):
        mnlist[m,i] = 1

    for i in range(len(puddles)):
        mnlist[puddles[i][0],puddles[i][1]] = -1

    for i in range(m-1,0,-1):
        for j in range(n-1,0,-1):
                if mnlist[i,j] == -1:
                    continue
                elif mnlist[i+1,j] != -1 and mnlist[i,j+1] != -1:
                    mnlist[i,j] = mnlist[i+1,j] + mnlist[i,j+1]
                elif mnlist[i+1,j] == -1 and mnlist[i,j+1] != -1:
                    mnlist[i,j] = mnlist[i,j+1]
                elif mnlist[i+1,j] != -1 and mnlist[i,j+1] == -1:
                    mnlist[i,j] = mnlist[i+1,j]
                elif mnlist[i+1,j] == -1 and mnlist[i,j+1] == -1:
                    mnlist[i,j] = -1
    print(mnlist)
    return mnlist[1,1]
