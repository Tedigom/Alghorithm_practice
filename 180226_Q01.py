# -*- coding: utf-8 -*-
# python3 180226_Q01.py

def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    count = 0
    summation = 0
    for i in list:
        summation += i
        count += 1
    return summation/count

list = [0,1,2,3]
print(average(list))
