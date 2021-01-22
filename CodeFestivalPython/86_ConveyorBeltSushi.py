"""
쉔은 회전초밥집에 갔습니다.
초밥집에 간 쉔은 각 초밥에 점수를 매기고 낮은 점수의 순서로 초밥을 먹으려 합니다.
이때 n 위치에 놓여진 초밥을 쉔은 접시가 몇 번 지나가고 나서 먹을지 출력하세요.

1. 초밥은 놓여진 위치에서 옮겨지지 않습니다.
2. 지나간 초밥은 나머지 초밥이 지나간 후에 다시 돌아옵니다.
3. 초밥은 1개 이상 존재합니다.

예:
A, B, C, D, E 초밥이 있고 각 점수가 1, 1, 3, 2, 5 일 때 3번째(C초밥)을 먹게 되는 순서는
1인 초밥 A와 B를 먹고 다음 2인 D 초밥을 먹어야 됩니다.
A B C D E 의 순서로 접시가 도착하지만 C가 도착했을때 먹지 못하는 상황이 옵니다.
2점을 주었던 D를 먼저 먹어야 C를 먹을 수 있습니다.
즉, A B C D E **C** , 접시가 5번 지나가고 먹게 된다.

**입력**
point = [1,1,3,2,5]
dish = 3

**출력**
5

**입력**
point = [5,2,3,1,2,5]
dish = 1

**출력**
10
"""


# point: 각 접시별 점수가 들어있는 배열
# dish: 먹고자하는 접시의 위치
# n 위치에 놓여진 초밥을 몇 번 지나고야 먹을 수 있는지 반환한다.
def conveyor_belt_sushi(point, dish):
    # 초밥을 먹으면 MAX 로 표시한다.
    MAX = 987654321
    # count: 움직인 횟수
    # pos: 먹으려는 위치
    # min_score: 가장 낮은 점수
    count = 0
    pos = -1
    min_score = min(point)
    # 배열의 시작은 0부터 시작이므로 -1을 해준다.
    dish -= 1
    while True:
        # 먹으려는 위치가 point 범위를 넘어가지 않도록 한다.
        if pos >= len(point):
            pos -= len(point)
        # 가장 낮은 점수의 접시를 받은 경우
        if point[pos] == min_score:
            # 종료 조건: 현재 먹으려는 위치(pos)와 먹으려는 위치(dish)와 같은 경우
            if pos == dish:
                break
            # 먹고자 하는 접시의 위치(dish) 가 아닌 경우 즉시 먹는다.
            point[pos] = MAX
            count += 1
            min_score = min(point)
        # 가장 낮은 점수의 접시가 아닌 경우, 이미 먹은 위치가 아니면 count 를 센다.
        elif point[pos] != MAX:
            count += 1
        # 위치를 증가한다.
        pos += 1
    return count - 1


# point: 각 접시별 점수가 들어있는 배열
# dish: 먹고자하는 접시의 위치
def another_solution(point, dish):
    # 배열 순서는 0부터 시작하므로 -1 해준다.
    dish -= 1
    answer = 0
    # 오름차순으로 정렬
    s = sorted(point)
    # point 제일 앞의 점수를 추출하여 p에 넣는다. 즉, 앞에 도착한 접시의 점수.
    # pop 과 append 를 활용해 구현한다.
    while True:
        p = point.pop(0)
        # 현재 s[0] 은 point 배열에서 가장 작은 값을 갖고 있다.
        # 현재 가장 낮은 점수를 가지고 있는 접시가 앞에 도착했다면 먹는다.
        if s[0] == p:
            # 앞에 도착한 접시가 선택한 접시라면 먹고 반복문을 종료한다.
            if dish == 0:
                break
            # 선택한 접시를 움직인다.
            dish -= 1
            # 한 접시를 먹었으므로 접시 하나가 줄어든다.
            s.pop(0)
        else:
            # 접시 위 초밥을 먹을 수 있는 조건이 충족되지 않아 그대로 둔다.
            # pop 했던 것을 다시 append 한다.
            point.append(p)
            # 만약 선택한 접시가 앞에 도착했다면 맨뒤로 보내고, 그렇지 않다면 한 칸 당긴다.
            dish = len(point) - 1 if dish == 0 else dish - 1


if __name__ == '__main__':
    p = list(map(int, input().split()))
    d = int(input())
    print(conveyor_belt_sushi(p, d))
