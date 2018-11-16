# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

from functools import cmp_to_key

def sortingByMe(n1, n2):
    return  int(n2 + n1) - int(n1 + n2)

def solution(numbers):
    if max(numbers) == 0:
        return '0'
    numbers = list(map(str,numbers))
    numbers.sort(key = cmp_to_key(sortingByMe))

    return ''.join(numbers)


'''
What I learned

1. map 함수의 활용 -> map(f, literable) 은 함수와 자료형을 입력으로 받는다.
-> map은 f에의해 수행된 결과를 묶어 리턴한다.  : numbers의 모든 자료형을 string으로 바꿈

2. from functools import cmp_to_key --> sorting을 내가 만든 함수로 sorting 할수 있게 해준다.
numbers.sort(key= cmp_to_key(myFunction))



'''
