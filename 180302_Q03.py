# -*- coding: utf-8 -*-
# python3 180302_Q03.py

'''
rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는
[]를 리턴하는 함수를 완성하세요. 예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고,
[10, 8, 22]면 [10, 22]를 리턴 합니다.
'''

def rm_small(mylist):
  new_list = []
  for i in range(len(mylist)):
      new_list.append(mylist[i])

  new_list.sort()
  distractedValue = new_list[0]
  mylist.remove(distractedValue)
  return mylist


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]

print("결과 {} ".format(rm_small(my_list)))

'''
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

def rm_small(mylist):
    mylist.pop(mylist.index(min(mylist)))
    return mylist
'''
