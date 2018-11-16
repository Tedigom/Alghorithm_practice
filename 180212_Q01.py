# -*- coding: utf-8 -*-

'''
99개의 값을 저장할 수 있는 배열 item[0],item[1], ... , item[98]이 있다. 1부터 100까지
값이 들어있는 집합 {1...100}에서 무작위로 수를 꺼내서 배열에 저장했다. 집합에 들어있는 원소의 수는
100개인데 반해서 배열의 값을 99개까지만 저장할 수 있으므로 집합안에 하나의 숫자가 남았다.
남은 것이 어느 수인지 확인할 수 있는 프로그램을 작성하라.
'''

import random

item_storage = range(99) #storage의 배열 ( 0~ 99 )

item_list = range(101)
del(item_list[0]) # itemlist에서 0을 지움
random.shuffle(item_list) # 무작위로 itemlist를 섞음
del(item_list[-1]) # list의 마지막 항목을 지움으로써 item_list와 item_storage의 갯수를 맞춤

tuple_list = []

for i in item_storage:
    tuple_list.append((i,item_list[i])) # item_list와 item_storage tuple을 짝지어줌
    # 어떻게 짝지어지는지만 프로그래밍( 실제로는 필요없는 코드 )


whole_sum = 5050 #1~100 까지의 sum
item_list_sum = sum(item_list,0.0) # item list 내의 모든 수의 합

print("남은 수는 : {}".format(whole_sum - item_list_sum))
