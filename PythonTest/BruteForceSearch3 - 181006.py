# https://programmers.co.kr/learn/courses/30/lessons/42841?language=python3
import itertools as it
def solution(baseball):
    alldigits = [1,2,3,4,5,6,7,8,9]
    correct0 = []
    correct1 = []
    correct2 = []
    correct3 = []
    #분류
    for i in range(len(baseball)):
        if baseball[i][1] + baseball[i][2] == 0:
            correct0.append(baseball[i])
        elif  baseball[i][1] + baseball[i][2] == 1:
            correct1.append(baseball[i])
        elif  baseball[i][1] + baseball[i][2] == 2:
            correct2.append(baseball[i])
        else:
            correct3.append(baseball[i])

    #0스트라이크, 0볼일때 후보군 삭제
    if len(correct0)>0:
        for i in range(len(correct0)):
            mid = list(str(correct0[i][0]))
            mid = list(map(int, mid))
            if mid[0] in alldigits:
                alldigits.remove(mid[0])
            if mid[1] in alldigits:
                alldigits.remove(mid[1])
            if mid[0] in alldigits:
                alldigits.remove(mid[2])

    if len(correct3)>0:
        mid = list(str(corrrect3[0][0]))
        alldigits= []
        alldigits.append(mid[0])
        alldigits.append(mid[1])
        alldigits.append(mid[2])

    def ballCount(n1, n2):
        r = [0,0]
        n1,n2 = str(n1),str(n2)
        for i in range(len(n1)):
            if n1[i] == n2[i]: r[0] += 1
            elif n1[i] in n2: r[1] += 1
        return r

    alldigits = map(str, alldigits)
    candidates = list(map(''.join, it.permutations(alldigits,3)))

    answer = []
    result = []
    for i in range(len(candidates)):
        for j in range(len(baseball)):
            if ballCount(baseball[j][0],candidates[i]) == [baseball[j][1],baseball[j][2]]:
                answer.append(candidates[i])

    for i in range(len(answer)):
        if answer.count(answer[i]) == len(baseball):
            if answer[i] not in result:
                result.append(answer[i])

    return len(result)

'''
What I learned

문제의 조건이 123~ 987까지였기때문에 완전탐색이 가능한 문제였다.
굳이 처음에 거르지 않아도, 123 ~ 987까지의 값을 가지고 완전탐색을 하면 됐었다.
--> ballcount 함수를 통해서 조건과 일일이 비교.

'''
