# answer 1
def calculateAllDigits(b):
    a  = 1
    splitNum = []
    digitSum = 0
    for i in range(0,b,1):
        a = a*2

    while a>0:
        b  =a%10
        a =int(a/10)
        splitNum.append(b)

    for i in splitNum:
        digitSum += i
    return digitSum


# answer 2
def printMultipleList(a = []):
    for i in a:
        for j in range(1,10,1):
            print(str(i)+" X "+str(j)+" = "+str(i*j))

# answer 3
def compareTwoLists(listOne=[], listTwo=[]):
    accord = []
    for i in listOne:
        for j in listTwo:
            if i == j:
                accord.append(i)

    print(accord)

# answer 4
def sumAllValuesBetweenVariables(a,b):
    sum = 0
    for i in range(a+1,b,1):
        sum += i

    print(sum)

# answer 6
def makeOppositeCharacter(a : str):
    result = ""
    for i in a:
        if i == i.upper():
            result += i.lower()
        else :
            result += i.upper()
    print(result)

# answer 7
def averagelengthOfWord(a : str):
    wordList = a.split(" ")
    lengthSum = 0
    for i in wordList:
        lengthSum += len(i)
    result = lengthSum/len(wordList)
    print(result)

# answer8
def sumOfmultipleunder100():
    sum = 0
    for i in range(0,101,1):
        if (i%3 == 0 or i%5 == 0):
            sum += i
    print(sum)

# answer9
from operator import eq

def printNumOfLeeHojun(value=[]):
    result = 0
    for i in value:
        if eq(i,'이호준') == True:
            result +=1
    print(result)

# answer10
def printAllHojun(value = []):
    hojuns = []
    for i in value:
        if i.find('호준') != -1 :
            hojuns.append(i)
    print(hojuns)

printAllHojun(['이호준','강호준','이호준','준호준','이호준','이호준이다','호준리','이호중'])
