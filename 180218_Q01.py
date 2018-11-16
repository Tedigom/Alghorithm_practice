# -*- coding: utf-8 -*-
# python3 180218_Q01.py

# 정렬 : Quick 정렬
''' 정렬 알고리즘 중에서 가장 널리 알려져 있는 것 중 하나가 퀵 정렬이다. 퀵정렬은 토니호어가 60년대에 발명한
알고리즘으로 '재귀'를 토대로 만들어진 정렬 기법이다. 퀵 정렬 알고리즘의 골격은 다음과 같은 작업으로 이루어진다.

1. 리스트에서 x를 '잘'고른다.
2. [분할]x보다 작은 값들은 왼쪽리스트, 큰값들은 오른쪽 리스트에 속한다.
3. 왼쪽 리스트에 대해서 재귀적으로 퀵 정렬을 수행한다.
4. 오른쪽 리스트에 대해서 재귀적으로 퀵 정렬을 수행한다.
5. [점령] 정렬이 끝난 왼쪽 리스트, x, 오른쪽 리스트를 모두 하나로 이어 붙인다.

이때 x가 최솟값이나 최댓값인 경우는 최악의 경우(worst case)이므로, x를 잘 고르는 것이 중요하다.


<문제>
정수를 저장하고 있는 배열 'array'가 주여졌다. 이 array에 저장되어있는 원소(element)들이 순서대로
정렬되어있으면 1을 리턴하고, 정렬되어있지 않으면 0을 리턴하는 함수를 작성하라

int isSorted(int* array, int length)
'''

def isSorted(array):

    for index,value in enumerate(array):
        if index < len(array)-1:
            if array[index] >= array[index+1]:
                print(array[index],array[index+1])
                print("정렬되어있지 않음")
                return 0

    print("정렬되어 있음")
    return 1


givenArray = [0,1,2,3,4,6,9]

isSorted(givenArray)
