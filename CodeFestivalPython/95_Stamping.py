"""
빈 종이에 stamp 모양으로 생긴 도장을 90*k 도로 회전하며 찍습니다.
도장은 N*N 크기이며 각 도장이 찍히는 부분은 1이상의 자연수와 도장이 찍히지 않는 0으로 이루어져 있습니다.

도장의 크기 N과,
종이에 찍힌 도장 횟수를 표현한 stamp 배열과,
얼만큼 회전할 것인지를 알려주는 회전수 k를 입력받았을 때
각 위치에서 몇 번 도장이 찍혔는지 그 결과값을 출력하세요

1 1 1 2             0 1 2 1
2 0 0 0   90도 회전   0 1 0 1
1 1 1 1  ---------> 0 1 0 1
0 0 0 0             0 1 0 2

1 1 1 2       0 1 2 1       1 2 3 3
2 0 0 0   +   0 1 0 1   =   2 1 0 1
1 1 1 1       0 1 0 1       1 2 1 2
0 0 0 0       0 1 0 2       0 1 0 2

## 입력 예시)

도장 = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]

회전 = 1
print(solution(도장,회전))

###출력
[[1, 2, 3, 3], [2, 1, 0, 1], [1, 2, 1, 2], [0, 1, 0, 2]]
"""

"""
90도 회전시켰을 때
0, 0 -> 0, 3
0, 1 -> 1, 3
0, 2 -> 2, 3
0, 3 -> 3, 3

1, 0 -> 0, 2
1, 1 -> 1, 2
1, 2 -> 2, 2
1, 3 -> 3, 2

...

i, j = j, n - 1 - i
"""


# stamp: 도장, k: 회전수. 90 * k 도 회전
# stamp 를 90 * k 도 회전 시켰을 때 각 위치에서 몇 번 도장이 찍혔는지 그 결과값을 반환한다.
# 만약 k가 2일 경우, 각 도장이 찍힌 횟수는 '처음 + 90도 회전했을 때 + 180도 회전했을 때' 이다.
def stamping(stamp, k):
    n = len(stamp)  # 도장의 크기: n * n
    answer = [[0] * n for _ in range(n)]
    # 처음 도장이 찍힌 횟수를 더한다.
    answer = add_stamp(stamp, answer)
    # stamp 를 90도씩 k 번 회전시켜 각 위치에서 찍힌 도장의 갯수를 더한다.
    for i in range(k):
        answer = add_stamp(stamp, rotate_stamp(answer))
    return answer


# 두 stamp 의 합을 구한다.
def add_stamp(stamp, another_stamp):
    for i in range(len(stamp)):
        for j in range(len(stamp)):
            another_stamp[i][j] = stamp[i][j] + another_stamp[i][j]
    return another_stamp


# stamp 를 90도씩 회전시킨다.
def rotate_stamp(stamp):
    n = len(stamp)  # 도장의 크기: n * n
    rotated_stamp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_stamp[j][n - 1 - i] = stamp[i][j]
    return rotated_stamp


"""
======== using numpy ======== 
"""
import numpy as np


# stamp 를 k 번씩 90도 회전하면서 각 위치에서 몇 번의 도장이 찍혔는지 계산한다.
def stamping_using_numpy(stamp, k):
    # 처음의 도장의 갯수를 더하기 위해 stamp 와 같은 numpy array 로 초기화
    answer = np.array(stamp)
    for i in range(1, k + 1):
        # 시계방향으로 k 번 회전하면서 stamp 가 찍힌 횟수를 더한다.
        answer = np.add(answer, np.rot90(stamp, i, axes=(1, 0)))
    return answer.tolist()  # 리스트 형태로 반환


if __name__ == '__main__':
    N = int(input('도장의 크기: '))
    s = []  # stamp
    for _ in range(N):
        s.append(list(map(int, input().split())))
    rotation_num = int(input('회전수: '))  # 회전수
    print(stamping(s, rotation_num))
    print(stamping_using_numpy(s, rotation_num))
