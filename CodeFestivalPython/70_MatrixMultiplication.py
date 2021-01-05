"""
행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고
곱할 수 있다면 그 결과를, 곱할 수 없다면 -1을 출력하는 프로그램을 만들어주세요.

* 라이브러리는 사용을 금지합니다.

**입력**
a = ([1, 2],   b = ([1, 3],  -> ([1*1+2*2 = 5,  1*3+2*4 = 11],
     [3, 4],        [2, 4]       [3*1+4*2 = 11, 3*3+4*4 = 25],
     [5, 6])                     [5*1+6*2 = 17, 5*3+6*4 = 39])


**출력**
([5,11], [11,25], [17, 39])
"""


def matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        return -1

    row = len(a)
    col = len(b[0])
    result = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(len(a[0])):
                result[i][j] += a[i][k] * b[k][j]

    return result


if __name__ == '__main__':
    A = ([1, 2], [3, 4], [5, 6])
    B = ([1, 3], [2, 4])
    print(matrix_multiplication(A, B))
