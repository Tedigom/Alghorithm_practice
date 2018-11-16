#https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3#

def solution(phone_book):
    pb_organized = sorted(phone_book,key= lambda x:len(x))

    for i in range(len(pb_organized)):
        for j in range(i+1,len(pb_organized)):
            if pb_organized[i] in (pb_organized[j])[0:len(pb_organized[i])]:
                return False
    else  :
        return True

'''
What I learned

1. sorted + lambda 조합
sortList = sorted(messyList, key= lambda x:len(x))
key = lambda x: ~~ 등으로 어떤 기준으로 sorting 할 것인지 정할수 있다.

2. 문자열 안에서 in 은 포함되어있는지를 바로 판단해준다.
3. 문자열에서 [0: ~]으로 slicing을 할 수 있다.

'''

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

'''
Further Study - What I learned from other's code

1.zip 함수
list(zip([1,2,3], [4,5,6]))
-> [(1,4),(2,5),(3,6)] 으로 자료형을 묶어줄 수 있다.
2. in 보다 startswith를 쓰는것이 접두어 문제에서는 더 알맞다.
'''
