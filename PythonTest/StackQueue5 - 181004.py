# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):
    remain =[]
    dayList = []

    for i in range(len(progresses)):
        plist = [100]*len(progresses)
        remain.append(plist[i]-progresses[i])

    for i in range(len(speeds)):
        if(remain[i] % speeds[i] == 0):
            dayList.append(remain[i] // speeds[i])
        else:
            dayList.append(remain[i]//speeds[i]+1)
## 걸리는 시간 리스트 완성
    answer = []
    while(len(dayList)>0):
        cnt = 0
        for i in range(len(dayList)):
            if dayList[0] < dayList[i]:
                break;
            cnt += 1

        for i in range(cnt):
            dayList.pop(0)
        answer.append(cnt)
    return answer

'''
what I learned

1. 리스트와 리스트사이에서 각 원소들의 계산 --> numpy를 이용할 수 있다.
numpy.array(lista - listb) ..
2. 길이가 n이고 모든 원소가 a인 배열을 만들려면 -> [a]*n 을 하면 된다.
'''
