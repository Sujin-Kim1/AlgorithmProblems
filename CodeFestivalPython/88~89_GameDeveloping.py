"""
지식이는 게임을 만드는 것을 좋아합니다. 하지만 매번 다른 크기의 지도와 장애물을 배치하는데 불편함을 겪고있습니다.
이런 불편함을 해결하기 위해 **지도의 크기와 장애물의 위치, 캐릭터의 위치만 입력하면 게임 지형을 완성해주는 프로그램**을 만들고 싶습니다.
지식이를 위해 게임 지형을 만드는 프로그램을 작성해야 합니다.
또한, 움직임을 입력했을 때 마지막 캐릭터의 위치를 반영한 지도를 보여주고 위치를 반환하는함수를 작성해주세요.


가로:n / 세로:m 크기가 주어집니다.
지형의 테두리는 벽으로 이루어져 있습니다.
캐릭터가 있는 좌표가 배열형태로 주어집니다.
장애물이 있는 좌표가 2차원 배열 형태로 주어집니다.
지도는 n x m 크기의 배열이며 배열안의 값은
   -움직일수 있는 공간(0)
   -캐릭터(1)
   -벽(2)
3개로 구분되어 있습니다.
캐릭터의 움직임은 {상:1,하:2,좌:3,우:4} 로 정수로 이루어진 배열이 들어갑니다.
벽과 장애물은 통과할 수 없습니다.

입출력 예시)
**입력**
가로 = 4
세로 = 5
캐릭터위치 = [0, 0]
장애물 = [[0, 1], [1, 1], [2, 3], [1, 3]]
움직임 = [2, 2, 2, 4, 4, 4]

**출력**
캐릭터 이동 전 지도
[2, 2, 2, 2, 2, 2]
[2, 1, 2, 0, 0, 2]
[2, 0, 2, 0, 2, 2]
[2, 0, 0, 0, 2, 2]
[2, 0, 0, 0, 0, 2]
[2, 0, 0, 0, 0, 2]
[2, 2, 2, 2, 2, 2]

캐릭터 이동 후 지도
[2, 2, 2, 2, 2, 2]
[2, 0, 2, 0, 0, 2]
[2, 0, 2, 0, 2, 2]
[2, 0, 0, 0, 2, 2]
[2, 0, 0, 0, 1, 2]
[2, 0, 0, 0, 0, 2]
[2, 2, 2, 2, 2, 2]
"""

"""
input  -> w * h
output -> (w+2) * (h+2)
 
<테두리>
-> [0][0]   ~ [0][w+1]   : 상
-> [h+1][0] ~ [h+1][w+1] : 하
-> [0][0]   ~ [h+1][0]   : 좌 
-> [0][w+1] ~ [h+1][w+1] : 우
"""


# width: 가로, height: 세로, character: 캐릭터 위치, obstacle: 장애물 위치
def make_game_board(width, height, character, obstacle):
    # 테두리를 표현하기 위해 (width + 2) * (height + 2) 의 맵을 생성한다.
    game_board = [[0 for x in range(width + 2)] for y in range(height + 2)]
    # 테두리 표현
    for y in range(width + 1):
        for x in range(height + 1):
            game_board[0][x] = 2  # 위
            game_board[y][0] = 2  # 왼쪽
            game_board[height + 1][x] = 2  # 아래
            game_board[y][width + 1] = 2  # 오른쪽
    # 캐릭터 위치
    game_board[character[0] + 1][character[1] + 1] = 1
    # 장애물 위치 (캐릭터가 있을 시 캐릭터는 그대로)
    for obs in obstacle:
        game_board[obs[0] + 1][obs[1] + 1] = 2 if game_board[obs[0] + 1][obs[1] + 1] != 1 else 1
    return game_board


# game_board: 게임 보드, moving: 움직임
# {상: 1, 하: 2, 좌: 3, 우: 4}
def move(game_board, moving, character):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    # 테두리가 추가되었으므로 x, y 의 위치를 1만큼 증가한다.
    character[0], character[1] = character[0] + 1, character[1] + 1
    # 캐릭터의 이동 후 게임 보드를 업데이트 한다.
    # 움직임의 번호와 dy, dx 의 인덱스를 이용해 이동 후의 캐릭터 위치를 결정한다.
    for m in moving:
        # 리스트의 인덱스는 0부터 시작하므로 1씩 빼준다.
        m -= 1
        y = character[0] + dy[m]
        x = character[1] + dx[m]
        # 장애물이 아니면 움직인다.
        if game_board[y][x] != 2:
            # 기존의 캐릭터 위치는 움직일 수 있는 공간으로 바뀐다.
            game_board[character[0]][character[1]] = 0
            # 이동 후 캐릭터의 위치를 저장한다.
            game_board[y][x] = 1
            # 캐릭터의 위치를 업데이트 한다.
            character[0] = y
            character[1] = x


if __name__ == '__main__':
    w = 4
    h = 5
    c = [0, 0]
    o = [[0, 1], [1, 1], [2, 3], [1, 3]]
    g = make_game_board(w, h, c, o)
    m = [2, 2, 2, 4, 4, 4]

    print('캐릭터 이동 전 지도')
    for i in range(len(g)):
        print(g[i])

    move(g, m, c)
    print('캐릭터 이동 후 지도')
    for i in range(len(g)):
        print(g[i])

