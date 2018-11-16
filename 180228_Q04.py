# -*- coding: utf-8 -*-
# python3 180228_Q04.py

def fibonacci(num):
    answer = 0
    if num == 0:
       	answer = 0
    elif num == 1 :
    	answer = 1
    else:
        answer = fibonacci(num-1)+fibonacci(num-2)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
