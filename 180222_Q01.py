# -*- coding: utf-8 -*-
# python3 180222_Q01.py

'''
1. map() 함수
map(f, iterable)은 함수 (f)와 반복 가능한(iterable) 자료형을 입력받는다.map은 입력받은
자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.


def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

이와 같은 형태의 코드를

def two_times(x): return x*2
list(map(two_times,[1,2,3,4]))
형태로 바꿀 수 있다.


2. split() 함수
a = "I have a dog"
a.split() # ['I','have','a','dog']
형태로 나누어준다.
b = "1:2:3:4"
b.split(':') #['1','2','3','4']

'''

'''
문제 : 두 수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''


# a = input("a 를 입력하세요")
# b = input("b 를 입력하세요")
# print(int(a)+int(b))
# 를 아래와 같이 변형할 수 있다.

a,b = map(int, input().split())
print(a+b)
