# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

def solution(clothes):
    categoryList = []
    categoryDict = {}
    answer = 1

    for i in range(len(clothes)):
        category = clothes[i][1]
        if category in categoryDict:
            categoryDict[category] += 1
        else:
            categoryDict[category] = 1

    for item in categoryDict:
        answer = answer*(categoryDict[item]+1)

    return answer-1

'''

What I learned

1. 리스트 내에서 원소의 갯수를 알고 싶을때 --> Dictionary로 키값에 대한 value를 정리한 후
for 문을 통해 뽑아냄.
2. value = Dict[key]

3. collection - Counter

myList = [1,2,3,4,1,4,1]
result = Counter(myList) ===> result = Counter({1:3, 4:2, 2:1, 3:1})
for key in result:
    print key, result[key]  ==> 1 3/ 2 1/ 3 1/ 4 2

result = Counter(myList).values() => [3,1,1,2]
'''
