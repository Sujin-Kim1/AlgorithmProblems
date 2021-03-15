/**
 * Question: https://www.algospot.com/judge/problem/read/BOARDCOVER
 * */

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

// 주어진 칸을 덮을 수 있는 네 가지 방법
// 블록을 구성하는 세 칸의 상대적 위치 (dy, dx)의 목록
const int coverType[4][3][2] = {
        {{0, 0}, {1, 0}, {0, 1}},  // 0
        {{0, 0}, {0, 1}, {1, 1}},  // 1
        {{0, 0}, {1, 0}, {1, 1}},  // 2
        {{0, 0}, {1, 0}, {1, -1}}  // 3
};

// board(y, x)를 type 번 방법으로 덮거나, 덮었던 블록을 없앤다.
// delta = 1 이면 덮고, -1이면 덮었던 블록을 없앤다.
// 만약 블록이 제대로 덮이지 않은 경우
// (게임판 밖으로 나가거나, 겹치거나, 검은 칸을 덮을 때) false 를 반환한다.
int set(vector<vector<int> > &board, int y, int x, int type) {

}

// board 의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환한다.
// board[i][j] = 1 이미 덮인 칸 혹은 검은 칸
// board[i][j] = 0 아직 덮이지 않은 칸
int cover(vector<vector<int> > &board, int y, int x) {

}

int main() {
    int C;  //  테스트 케이스의 수 C (C <= 30)
    int H, W;  // 2개의 정수 H, W (1 <= H,W <= 20)
    char shapeOfBoard;  // 게임판의 모양

    cin >> C;

    for (int i = 0; i < C; i++) {
        cin >> H >> W;
        vector<vector<int> > board(H, vector<int> (W, 0));  // H * W 크기의 게임판

        // 게임판을 입력 받는다.
        for (int h = 0; h < H; h++) {
            for (int w = 0; w < W; w++) {
                cin >> shapeOfBoard;
                // 게임판의 모양이 #. 즉, 검은 칸이면 0을, 아니면 1을 저장한다.
                board[h][w] = shapeOfBoard == '#' ? 0 : 1;
            }
        }

    }

}