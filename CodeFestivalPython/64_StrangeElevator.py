"""
정량 N에 정확히 맞춰야만 움직이는 화물용 엘레베이터가 있습니다.
화물은 7kg, 3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.

예를 들어 정량이 24kg 이라면 3kg 8개를 옮기는 것 보다는
7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.

**입력**
정량 N이 입력됩니다.

**출력**
가장 적게 옮길 수 있는 횟수를 출력합니다.
만약 어떻게 해도 정량이 N이 되지 않는다면 -1을 출력합니다.
"""


def strange_elevator(N):
    for i in range(N // 7, -1, -1):
        remainder = N - (7 * i)
        if remainder % 3 == 0:
            return print(i + remainder // 3)
    return print(-1)


def another_solution(N):
    result = 0
    while True:
        if N % 7 == 0:
            result += N // 7
            print(result)
            break
        N -= 3
        result += 1
        if N < 0:
            print(-1)
            break


if __name__ == '__main__':
    n = int(input())
    strange_elevator(n)
    another_solution(n)
