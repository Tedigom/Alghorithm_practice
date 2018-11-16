# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
def solution(brown, red):
    mnPlus=int((brown-4)/2)
    mnBy = red

    candidates = []
    answer = []
    for i in range(mnPlus):
        candidates.append([i,mnPlus-i])

    for i in range(len(candidates)):
        if candidates[i][0] * candidates[i][1] == mnBy:
            answer.append([candidates[i][0], candidates[i][1]])

    if len(answer) == 1:
        tempA = answer[0][0]
        tempB = answer[0][1]
        tempA += 2
        tempB += 2
        answer = []
        answer = [tempA , tempB]
    elif answer[0][0] > answer[1][0]:
        tempA = answer[0][0]
        tempB = answer[0][1]
        tempA += 2
        tempB += 2
        answer = []
        answer = [tempA , tempB]
    else :
        tempA = answer[1][0]
        tempB = answer[1][1]
        tempA += 2
        tempB += 2
        answer = []
        answer = [tempA , tempB]


    return answer

'''
What I learned

크게 어려운 문제는 아니었다. 다만 마지막에 처리하는 과정에서 함수를 쓰면 좀더 깔끔하게 나왔을 것이다.
'''

'''
How people do

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

'''            
