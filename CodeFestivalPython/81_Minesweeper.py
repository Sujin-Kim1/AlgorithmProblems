"""
지뢰를 찾는 문제입니다. 다음 그림처럼 깃발 주위에는 지뢰가 사방으로 있습니다. **깃발의 위치를 입력받아 지뢰와 함께 출력해주는 프로그램**을 만드세요.

- 아래 Case 외 예외 사항은 고려하지 않습니다.
(예를 들어 깃발이 붙어 있을 경우는 고려하지 않습니다.)
실력이 되시는 분들은 깃발이 붙어있을 상황까지 고려해주세요

입력
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0

출력
* f * 0 0
0 * 0 * 0
0 0 * f *
0 * f * 0
0 0 * 0 0
"""

# 지뢰 없이 깃발만 있는 리스트
flag = []
# 자뢰를 찾은 리스트
mines = [['0' for row in range(5)] for column in range(5)]
# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def minesweeper():
    for y in range(5):
        for x in range(5):
            # flag 를 발견한 경우 f 표시를 하고 주변에 지뢰 표시를 한다.
            if flag[y][x] == '1':
                mines[y][x] = 'f'
                for mines_pos in range(4):
                    next_y, next_x = y + dy[mines_pos], x + dx[mines_pos]
                    # 범위가 벗어난 경우 혹은 flag 인 경우
                    if (next_x < 0 or next_y < 0 or next_x >= 5 or next_y >= 5) or (mines[next_y][next_x] == 'f'):
                        continue
                    # 지뢰 표시
                    mines[next_y][next_x] = '*'


if __name__ == '__main__':
    for i in range(5):
        flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))
    minesweeper()

    print('----- flag -----')
    for i in range(5):
        for j in range(5):
            print(flag[i][j], end=' ')
        print()
    print('----- mines -----')
    for i in range(5):
        for j in range(5):
            print(mines[i][j], end=' ')
        print()
