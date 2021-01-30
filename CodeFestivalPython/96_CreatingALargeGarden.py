"""
수연이는 밭 농사를 시작하기로 마음을 먹었다. 집 앞 텃밭을 만들기로 하고 돌들을 제거하고 있는데 매우 큰 바위는 옮기지 못해 고심하고 있다.

이에 수연이는 다음과 같은 규칙을 정한다.

1. 바위를(바위는 '1'로 표기한다.) 피해 텃밭을 만들되 정사각형 모양으로 텃밭을 만든다.
2. 텃밭은 가장 넓은 텃밭 1개만 만들고 그 크기를 반환한다.
3. 만든 텃밭은 모두 '#'으로 처리한다.

<입출력 예시>

**입력**
0 0 0 0 0
0 1 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0

**출력**
3 X 3
0 0 # # #
0 1 # # #
0 1 # # #
0 0 1 0 0
0 0 0 1 0

**입력**
0 0 0 1 0
0 0 0 0 0
1 0 1 0 0
0 0 1 0 0
1 0 0 1 0

**출력**
2 X 2
# # 0 1 0
# # 0 0 0
1 0 1 0 0
0 0 1 0 0
1 0 0 1 0
"""
import numpy as np

# n * n 사이즈의 텃밭
GARDEN_SIZE = 0
garden = []  # 텃밭


# garden[y][x]에서 size * size 크기의 밭을 만들 수 있는지 확인한다.
# 바위가 하나라도 있으면 False 를 반환한다.
def is_possible(size, y, x):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if garden[i][j] == '1':
                return False
    return True


# 가장 넓은 텃밭의 한 변의 길이와 텃밭의 좌표를 반환한다.
def find_max_garden(size, y_start, x_start):
    for y in range(GARDEN_SIZE - size + 1):
        for x in range(GARDEN_SIZE - size + 1):
            # (size) * (size) 크기의 밭을 만들 수 있으면, (size+1) * (size+1) 크기도 가능한지 확인한다.
            if is_possible(size, y, x):
                y_start = y
                x_start = x
                return find_max_garden(size + 1, y_start, x_start)
            # 종료: 한 변의 길이가 size 인 밭을 만들 수 없으면 최대 크기는 size - 1이므로 이를 반환한다.
            elif y + size == x + size == GARDEN_SIZE:
                return size - 1, y_start, x_start
    # 모두 바위로 되어 있어 텃밭을 전혀 만들 수 없다.
    return size - 1, y_start, x_start


def creating_garden():
    size = 1  # 텃밭의 크기
    y_start = x_start = 0  # 텃밭의 시작 장소
    # 가장 넓은 텃밭의 크기와 시작 위치를 찾는다.
    size, y_start, x_start = find_max_garden(size, y_start, x_start)

    # 텃밭을 표시한다.
    for i in range(y_start, y_start + size):
        for j in range(x_start, x_start + size):
            garden[i][j] = '#'

    # 텃밭의 크기와 텃밭을 출력한다.
    print(size, 'X', size)
    print('\n'.join(' '.join(row) for row in garden))


"""
numpy 를 이용한 다른 방법
1) '역전된 상태의 텃밭' 을 구한다.
2) '역전된 상태의 텃밭' 의 (1, 1) 부터 시작해서 'min(왼쪽, 좌상단, 위쪽) + 1'을 적용한 '역전된 상태의 텃밭의 합'을 구한다.
   이때, 해당 값이 0이면 바위 때문에 텃밭을 만들 수 없으므로 무시한다.
3) '역전된 상태의 텃밭의 합' 에서 가장 큰 값을 갖는 곳이 텃밭의 위치이고, 그 값이 텃밭의 크기이므로 텃밭을 표시한다.

# 텃밭
[[0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0],
 [0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0]]

# 역전된 상태의 텃밭
[[1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1],
 [1, 0, 1, 1, 1],
 [1, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

# 역전된 상태의 텃밭의 합
[[1, 1, 1, 1, 1],
 [1, 0, 1, 2, 2],
 [1, 0, 1, 2, 3],
 [1, 1, 0, 1, 2],
 [1, 2, 1, 0, 1]]
"""


def another_solution():
    g = np.array(garden, int)  # 텃밭
    reversed_garden = np.array(np.where(g == 1, 0, 1), int)  # 역전된 상태의 텃밭
    # 역전된 상태의 텃밭의 합
    # min(왼쪽, 좌상단, 상단) + 1 을 함으로써, 만들 수 있는 텃밭의 최대 크기를 구한다.
    for y in range(1, GARDEN_SIZE):
        for x in range(1, GARDEN_SIZE):
            if reversed_garden[y][x] != 0:
                reversed_garden[y][x] = np.amin([reversed_garden[y][x - 1],
                                                 reversed_garden[y - 1][x - 1],
                                                 reversed_garden[y - 1][x]]) + 1
    # 최대 크기의 텃밭 사이즈
    size = np.max(reversed_garden)

    # 텃밭 표시
    g = np.array(garden, str)  # 텃밭을 표시하기 위해 str 으로 형변환
    garden_pos = np.where(reversed_garden == size)  # 텃밭의 위치
    garden_pos_y, garden_pos_x = garden_pos[0][0], garden_pos[1][0]  # 텃밭의 x, y 좌표
    g[garden_pos_y - size + 1: garden_pos_y + 1, garden_pos_x - size + 1: garden_pos_x + 1] = '#'  # 텃밭 표시

    # 텃밭 크기와 텃밭 출력
    print(size, 'X', size)
    print('\n'.join([' '.join(row) for row in g]))


if __name__ == '__main__':
    # 텃밭의 크기를 입력으로 받는다.
    GARDEN_SIZE = int(input('텃밭의 크기: '))
    # 텃밭의 데이터를 입력으로 받는다.
    for _ in range(GARDEN_SIZE):
        garden.append(input().split())
    # 가장 큰 텃밭을 만든 결과를 출력한다.
    another_solution()
    creating_garden()
