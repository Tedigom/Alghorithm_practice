# https://programmers.co.kr/learn/courses/30/lessons/42588?language=python3

def solution(heights):
    answer = []
    while(len(heights) > 0):
        popTop = heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > popTop:
                    answer.append(i+1)
                    break
            if i == 0 and heights[i]<= popTop:
                answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer

'''
what I learned

1. range --> (0,a,1) --> 0이상, a 미만 1씩증가
   거꾸로 할때 --> (a,-1,-1) --> a부터 0까지 1씩 감소
'''
