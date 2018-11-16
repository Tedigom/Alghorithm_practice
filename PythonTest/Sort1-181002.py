# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]-1
        pick = commands[i][2]-1

        arrayPart = array[start:end+1]
        arrayPart = sorted(arrayPart)
        print(arrayPart)
        answer.append(arrayPart[pick])

    return answer

'''
what I learned

array의 slicing은 start 이상 end 미만(end는 포함되지 않는다.) 으로 된다.
'''
