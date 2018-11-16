# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3#

import itertools as it
def solution(numbers):
    numberlist = list(numbers)
    numberlist1 = list(map(''.join, it.permutations(numberlist)))

    for i in range(len(numbers)-1):
        mid = list(map(''.join, it.combinations(numberlist, i+1)))
        for j in range(len(mid)):
                    num1 = list(map(''.join, it.permutations(mid[j])))
                    for k in range(len(num1)):
                        numberlist1.append(num1[k])
    # 모든 순열을 numlist1에 넣었다.
    num = []
    for i in range(len(numberlist1)):
        if int(numberlist1[i]) not in num:
            num.append(int(numberlist1[i]))
    print(num)
    for i in range(len(num)):
        for j in range(2,num[i],1):
            if num[i]%j ==0:
                num[i] = 0
                break

    while( 0 in num):
        num.remove(0)
    if 1 in num :
        num.remove(1)
    return len(num)
'''
What I learned
1. 순열(permutations) 쓰는 법 -> list(map(''.join, itertools.permutations(list)))
2. 조합(combinations) 쓰는 법 -> list(map(''.join, it.combinations(list, i)))

--> list(map(''.join, ))을 꼭 쓰도록하자. 아니면 처리하기가 힘듬.

3. for i in ~ 을 쓸때 웬만하면 그냥 range(len(a))를 쓰도록 하자.
for i in a 는 위험한듯.

4. itertools 쓰지 않고 조합을 푸는 방법 : 재귀를 이용 / 팩토리얼(재귀) 이용
재귀 이용방법 - 솔직히 잘 이해하지 못했다.

def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            print(i,b)
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)


        return result

'''
