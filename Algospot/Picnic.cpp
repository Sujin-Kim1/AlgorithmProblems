/**
 * Question: https://www.algospot.com/judge/problem/read/PICNIC
 * */

#include <iostream>
#include <cstring>

using namespace std;

bool areFriends[10][10];  // 친구인 학생들을 짝짓는다.

// n = 학생의 수
// taken[i] = i 번째 학생이 짝을 이미 찾았으면 true, 아니면 false
int countPairings(int n, bool taken[]) {
    // 남은 학생들 중 가장 번호가 빠른 학생을 찾는다.
    int firstFree = -1;
    for (int i = 0; i < n; i++) {
        if (!taken[i]) {
            firstFree = i;
            break;
        }
    }
    // 기저 사례: 모든 학생이 짝을 찾았으면 한 가지 방법을 찾았으니 종료한다.
    if (firstFree == - 1) return 1;
    // 이 학생과 짝지을 학생을 결정한다.
    int ret = 0;
    for (int pairWith = firstFree+1; pairWith < n; pairWith++) {
        if (!taken[pairWith] && areFriends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairings(n, taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    }
    return ret;
}

int main() {
    int C;  // 테스트 케이스의 수 (C <= 50)
    int n, m;  //  학생의 수 n (2 <= n <= 10) 과 친구 쌍의 수 m (0 <= m <= n*(n-1)/2)
    bool taken[10];  // taken[i] = i 번째 학생이 짝을 이미 찾았으면 true, 아니면 false
    int friend1, friend2;  // 친구인 학생들

    cin >> C;

    // Test Cases 실행
    for (int i = 0; i < C; i++) {
        // 배열 초기화
        memset(areFriends, 0, sizeof(areFriends));
        memset(taken, 0, sizeof(taken));

        cin >> n >> m;
        // m 개의 정수 쌍으로 서로 친구인 두 학생의 번호가 주어진다.
        for (int j = 0; j < m; j++) {
            cin >> friend1 >> friend2;
            areFriends[friend1][friend2] = areFriends[friend2][friend1] = true;
        }
        cout << countPairings(n, taken) << endl;
    }
}
