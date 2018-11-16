# -*- coding: utf-8 -*-
# python3 180302_Q04.py
'''
toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을
리턴하도록 함수를 완성하세요. 예를 들어 s가 try hello world라면 첫 번째 단어는 TrY,
두 번째 단어는 HeLlO, 세 번째 단어는 WoRlD로 바꿔 TrY HeLlO WoRlD를 리턴하면 됩니다.

주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.
'''

def toWeirdCase(s):
    resultList = []
    # 함수를 완성하세요
    for i in range(len(s.split())):
        for j in range(len(list(s.split()[i]))):
            if j%2==0:
                resultList.append(list(s.split()[i])[j].upper())
            else:
                resultList.append(list(s.split()[i])[j].lower())
        resultList.append(" ")
    del resultList[-1]
    return "".join(resultList)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));

'''
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''
