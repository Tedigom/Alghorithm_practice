# -*- coding: utf-8 -*-
# python3 180219_Q04.py

'''
재귀 ( recursion )
gcd 함수(유클리드 알고리즘) 에서 swap 함수를 호출하지 않게 만드는 방법?
재귀! --> 재귀는 가장 간결하고 미감이 풍부한 기법에 속한다. 아래의 코드는 재귀 기법을 이용한다.

C를 비롯하여 거의 모든 프로그래밍 언어에서 함수가 호출되면 함수가 호출된 장소를 가리키는 주소가 시스템
내부의 스택에 저장된다. 이것은 호출된 함수가 작업을 끝마치고 리턴될때 되돌아갈 위치를 기억해야 하기 때문이다.
재귀함수는 시스템 내부의 스택에 함수의 주소가 저장되어야 하기 때문에 함수가 재귀적으로 호출되는 횟수가
일정한 수를 넘게 되면 알고리즘의 실행 속도가 저하된다는 단점이 있다.

--> 내부 스택을 이용해서 함수가 호출된 지점을 정확하게 기억해야 하기 때문에 메모리의 사용이나 프로그램의
처리 속도 면에서 추가적인 부하가 걸린다. --> 직접 설계한 스택을 이용하거나 for나 while 같은
루프를 돌리는 방법을 선호하는 경우가 많다.

재귀는 명쾌하지만 무겁고 느리며, for나 while 루프를 직접 돌리는 방식은 가볍고 빠르지만 코드가 읽기 어렵고 멋이 없다는 단점이 있다.
이 두 가지 방법 사이에서 각자의 장점을 취하는 특이한 알고리즘이 존재하는데 이를 "꼬리 재귀(tail recursion"
이라고 불린다. 함수가 호출된 위치를 기억해 둘 필요가 없어서 재귀적 함수를 원래 함수의 꼬리 부분에서 호출하는
경우를 일컬어 '꼬리재귀'라고 말한다.
'''
# ex 1
def recursion_sum(n,m):
    if m>=n:
        return m+recursion_sum(n,m-1)
    else:
        rerurn 0


def tail_recursion_sum(total,n,m):
    if m>=n:
        return tail_recursion_sum(total+m,n,m-1)
    else:
        return total
