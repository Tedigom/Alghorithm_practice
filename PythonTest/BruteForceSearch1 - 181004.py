# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    def makeAnswerList(p, answers):
        a = []
        n = len(answers) // len(p)
        r = len(answers) % len(p)
        for i in range(n):
            for j in range(len(p)):
                a.append(p[j])
        for i in range(r):
            a.append(p[i])
        return a

    a1 = makeAnswerList(p1,answers)
    a2 = makeAnswerList(p2,answers)
    a3 = makeAnswerList(p3,answers)
    c = [0,0,0]

    for i in range(len(answers)):
        if a1[i] == answers[i]:
            c[0] += 1
        if a2[i] == answers[i]:
            c[1] += 1
        if a3[i] == answers[i]:
            c[2] += 1

    maxNum = max(c)
    answer = []
    for i in range(len(c)):
        if c[i] == maxNum:
            answer.append(i+1)
    return answer
