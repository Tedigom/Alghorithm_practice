# -*- coding: utf-8 -*-
# python3 180220_Q01.py

# RSA 알고리즘
# https://www.youtube.com/watch?v=bvW1p4GKv94 참고
'''
RSA  알고리즘은 다음과 같은 수학적인 기호와 개념으로 설명된다.
1. p와 q가 소수라고 했을때 n = pq를 계산한다.
2. p와 q에서 각각 1을 빼서 곱한다. 그것을 phi 라고 부른다.
(phi = (p-1)(q-1))
3. 다음 조건을 만족하는 e를 찾는다.
1 < e < phi , gcd(e, phi) = 1
4. 다음조건을 만족하는 d를 찾는다.
1 < d < phi, ed == 1 (mod phi)
5.(n,e)는 공개 키고, (n,d)는 개인 키다. p, q, phi 와 같은 값은 공개되지 않도록 한다.
'''

'''
문제 1
단일 연결리스트를 만들어보고 중간의 노드를 리스트에서 삭제하는 알고리즘을 만들어 보아라
'''
# 단일연결리스트 생성

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def init_list():
    global node1, node2, node3, node4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(333)
    node4 = Node("I am four")

    node1.next = node2
    node2.next = node3
    node3.next = node4


def Main():
    init_list()
    node = node1
    while node:
       print node.data,
       node = node.next

Main()

def delete_node(delete_data):
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == delete_data:
        node1 = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
           pre_node.next = next_node.next
           del next_node
           break
        pre_node = next_node
        next_node = next_node.next
