# -*- coding: utf-8 -*-
# python3 180213_Q01.py
''' 앞에서 읽으나 뒤에서 읽으나 똑같은 단어를 우리는 '회문' 이라고 부르고, 영어에서는 '팰린드롬(
palindrome)'이라고 한다. 우리말에서 '기러기'나 영어에서 'eye', 'madam' 등이 팰린드롬에
해당한다. 문자열을 입력받아서 입력된 문자가 팰린드롬인지 아닌지 여부를 확인하는 함수를 작성하라.
입력된 문자열이 팰린드롬이면 true를 리턴하고, 아니면 false를 리턴해야한다.'''


user_string = input('문자열을 입력해 주세요 > ')
user_list = list(user_string) # 받은 문자열을 리스트로 쪼갬

reverse_list = [] # 거꾸로 뒤집을 list

for i, val in enumerate(user_list):
     reverse_list.append(user_list[len(user_list)-i-1])


print(reverse_list)

if user_list == reverse_list :
    print("palindrome true")
else :
    print("palindrome false")


# 사실 a.reverse()   : a == 리스트 를 하여 비교하면 쉽게 할 수 있다. 하지만, reverse_list = user_list의
# 형태로 참조하여 할 경우 원래 값 user_list도 reverse 되어버리기 때문에 내용 요소를 append
# 시킨 다음에 reverse() 함수를 써야할 것으로 생각된다.



"""
*참고*

그루앤 버거 알고리즘

1. 숫자를 아무거나 골라라.
2. 그 수를 뒤집어라 ( 예를들어 13을 골랐다면 31로 뒤집는다.) 다음 뒤집힌 수를 원래 수에 더하라(13+31)
3. 그 수를 더한 결과가 펠린드롬이 아니라면, 2로 돌아가서 동일 과정을 반복한다. 두수를 더한 결과가
펠린드롬이라면 알고리즘을 종료한다.

대부분의 수가 어느정도 계산이 수행되고 나면 팰린드롬이 되는 것이 확인되었다.
하지만 제일 작으면서도 가장 끈질기게 버티는 수가 196이다. '196 알고리즘' 혹은 '196 문제'라고 널리 알려져있는
문제는 196이 앞의 알고리즘을 적용할 수 있을때 팰린드롬을 얻을수 있는가 하고 묻는 것을 의미한다.
196의 여정은 7천만개의 숫자로 이루어진 수까지 진행되었는데, 아직 팰린드롬이 나타날 조짐은 아직도 보이지 않는다.
"""
