"""
기린은 중국집에서 친구들과 만나기로 하고, 음식을 시켰습니다.
음식이 나오고 한참을 기다렸지만 만나기로 한 친구 2명이 오지 않았어요.

기린은 배가 너무 고파 혼자 음식을 먹기 시작합니다. 원형테이블에는 N개의 음식들이 있습니다.
한개의 음식을 다 먹으면 그 음식의 시계방향으로 K번째 음식을 먹습니다.
하지만 아직 오지 않은 친구들을 위해 2개의 접시를 남겨야 합니다.

**마지막으로 남는 음식은 어떤 접시인가요?**

입력은 2개의 정수로 이루어지며 공백으로 구분되어 입력됩니다.
첫번째 숫자가 음식의 개수 N, 두번째 숫자가 K 입니다.
첫번째 가져가는 음식이 K이며 나머지는 첫번째 음식으로부터 시계방향으로 가져갑니다.

입력
6 3


남은 음식들의 번호를 리스트 형태로 출력합니다.
출력
[3, 5]
"""


def circle_table(N, K):
    is_eaten = [False for i in range(N)]
    result = []
    idx = 0
    is_eaten[idx] = True

    while is_eaten.count(False) != 2:
        i = 1
        while i <= K:
            if idx + 1 >= N:
                idx -= N
                continue
            if not is_eaten[idx + 1]:
                i += 1
            idx += 1
        is_eaten[idx] = True

    for i in range(len(is_eaten)):
        if not is_eaten[i]:
            result.append(i + 1)
    return result


def another_solution(N, K):
    i = 0
    # q에 n 만큼의 숫자를 넣어준다.
    q = [i for i in range(1, n + 1)]

    while len(q) > 2:
        # 순환하다 i가 q의 길이보다 같거나 클 경우에 len(q)만큼 빼준다.
        if i >= len(q):
            i -= len(q)
        q.pop(i)
        i += k - 1
    return q


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(circle_table(n, k))
    print(another_solution(n, k))
