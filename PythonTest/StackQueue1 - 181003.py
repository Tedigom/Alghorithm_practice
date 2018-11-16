# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3

def solution(arrangement):
    steelStack = 0
    totalSteel = 0
    midAnswer = 0
    answer = 0
    isLaser = False

    for i in range(len(arrangement)-1):
        if arrangement[i] == '(' and arrangement[i+1] == ')':
            isLaser = True
            midAnswer += steelStack
        elif arrangement[i] == '(' and arrangement[i+1] == '(':
            steelStack += 1
            totalSteel +=1
        elif arrangement[i] ==')':
            if isLaser == True:
                isLaser = False
            else:
                steelStack -= 1


        if((i == len(arrangement)-2)  and arrangement[i] == ')'):
                steelStack -= 1

        if steelStack == 0:
            answer += midAnswer
            midAnswer = 0

    return answer+totalSteel


'''
what I learned

너무 오래걸렸다. 스택을 이용한 문제였는데, 제대로 쓰지 못한 느낌이었다.
이 문제를 푸는데의 아이디어는
* 기본전제 : 레이저 ==> steel의 갯수를 steel 갯수만큼 더 늘린다.

1. 우선 arrangement에서 레이저인지 아닌지를 파악한다.
2. 레이저가 아니라면 ( 는 steel의 시작임을 뜻한다.
3. 레이저가 아니라면 ) 는 steel의 끝임을 뜻한다.

for문을 len(arrangement)-1 까지 돌렸으므로, 맨끝이 레이저가 아닌 경우를 생각하여 예외처리를한다.
나오는 answer은 철의 증가량을 뜻하므로, totalsteel를 더해주어 답을 구한다.

아무리 생각해도 효율적인 아이디어는 아니었다.
아래에 다른 사람이 푼 코드를 첨부하여 분석해보겠다.
'''

def solution(arrangement):
    stack=[]
    answer=0
    for w in arrangement:
        if len(stack)==0:
            stack.append(True)
        elif w=='(':
            stack[-1]=False
            stack.append(True)
        else:
            if stack[-1]:
                answer+=len(stack)-1
            else:
                answer+=1
            stack.pop(-1)
    return answer
