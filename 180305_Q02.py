# -*- coding: utf-8 -*-
# python3 180305_Q02.py

'''
행렬의 곱셈은, 곱하려는 두 행렬의 어떤 행과 열을 기준으로, 좌측의 행렬은 해당되는 행, 우측의 행렬은
해당되는 열을 순서대로 곱한 값을 더한 값이 들어갑니다. 행렬을 곱하기 위해선 좌측 행렬의 열의 개수와
우측 행렬의 행의 개수가 같아야 합니다. 곱할 수 있는 두 행렬 A,B가 주어질 때, 행렬을 곱한 값을
출력하는 productMatrix 함수를 완성해 보세요.
'''

def productMatrix(mat1, mat2):
    result = [ len(mat2[0])*[0] for i in range (len(mat1)) ]

    for i in range (len(result) ):
        for j in range ( len(result[i]) ):
            for k in range ( len(mat1[i] ) ):
                result[i][j] += mat1[i][k]*mat2[k][j]

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));


'''
def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
'''
