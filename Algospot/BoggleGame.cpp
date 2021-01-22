/**
 * Sources: https://www.algospot.com/judge/problem/read/BOGGLE
 * */

#include <iostream>
#include <vector>
#include <cstring>

#define BOARD_SIZE 5

using namespace std;

// board: BOARD_SIZE * BOARD_SIZE 의 게임판
vector<string> board;

const int dy[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dx[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

// 보글 게임 판의 해당 위치에서 주어진 단어가 시작하는지를 반환
bool hasWord(int y, int x, const string &word) {
    // 게임판을 벗어난 경우
    if (y >= BOARD_SIZE || x >= BOARD_SIZE || y < 0 || x < 0) return false;
    // (y, x)에 있는 글자가 원하는 단어의 첫 글자가 아닌 경우
    if (board[y][x] != word[0]) return false;
    // word 의 길이가 1이면 성공
    if (word.size() == 1) return true;
    // word 의 길이가 1이 아닌 경우 원하는 단어를 찾는다.
    for (int direction = 0; direction < 8; direction++) {
        if (hasWord(y + dy[direction], x + dx[direction], word.substr(1))) return true;
    }
    return false;
}

int main() {
    // C: 테스트 케이스의 수 (C <= 50)
    int C;
    cin >> C;
    // 게임판의 모든 칸은 알파벳 대문자이며 크기는 BOARD_SIZE * BOARD_SIZE 이다.
    string s;
    for (int i = 0; i < BOARD_SIZE; i++) {
        cin >> s;
        board.push_back(s);
        s = "";
    }
    // N: 우리가 알고 있는 단어의 수 (1 <= N <= 10)
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        // 단어 입력
        string word;
        cin >> word;
        // hasWord 가 true 인지 false 인지 저장하는 bool 값
        bool result = false;
        for (int y = 0; y < BOARD_SIZE; y++) {
            for (int x = 0; x < BOARD_SIZE; x++) {
                if (hasWord(y, x, word)) {
                    result = true;
                    break;
                }
            }
        }
        cout << word << " " << (result? "YES" : "NO") << endl;
    }
}
