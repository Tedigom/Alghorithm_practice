# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities, location):
    answer = 0
    while True:
        if location == 0:
            if priorities[0] == max(priorities):
                break;
            else :
                mid = priorities.pop(0)
                priorities.append(mid)
                location = len(priorities)-1
        else:
            if priorities[0] == max(priorities):
                answer += 1
                priorities.pop(0)
                location -= 1
            else :
                mid = priorities.pop(0)
                priorities.append(mid)
                location -=1
    return answer+1

'''
what I learned
--> 문제를 복잡하게 만들지 말자 : 최대한 생각을 많이 하고, 종이에 시뮬레이션을 해 본 후 코딩을 시작하자.
변수가 너무 많아지면 힘들다.

'''
