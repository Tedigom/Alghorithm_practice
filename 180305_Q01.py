# -*- coding: utf-8 -*-
# python3 180305_Q01.py

'''
앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
예를들어 s가 토마토맛토마토이면 7을 리턴하고 토마토맛있어이면 3을 리턴합니다.
'''

def longest_palindrom(s):
    # 함수를 완성하세요
    palindromList = []
    for i in range(len(s)+1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                palindromList.append(i-j)

    return max(palindromList)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("기러기는예쁘다"))



'''
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))
'''
