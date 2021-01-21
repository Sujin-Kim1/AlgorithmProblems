/**
 * Sources: https://www.algospot.com/judge/problem/read/WILDCARD
 * */

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

// 와일드카드에 매치되는 파일들의 이름을 한 줄에 하나씩 아스키 코드 순서대로 저장한다.
vector<string> answer;

// -1: 답이 계산되지 않음
//  1: 해당 입력들이 서로 대응됨
//  0: 해당 입력들이 서로 대응되지 않음
// 1 <= 문자열의 길이 <= 100
int cache[101][101];
// 패턴과 문자열
string W, S;

// 와일드카드 패턴 W[w...]가 문자열 S[s...]에 대응되는지 여부를 반환한다.
bool matchMemoized(int w, int s) {
    // memoization
    int &ret = cache[w][s];
    // 기저 사례: 이미 계산한 값이면 그대로 반환한다.
    if (ret != -1) return ret;
    // W[w]와 S[s]를 맞춰나간다.
    if (w < W.size() && s < S.size() &&
        (W[w] == '?' || W[w] == S[s]))
        return ret = matchMemoized(w + 1, s + 1);
    // 더이상 진행할 수 없으면 왜 while 문이 끝났는지 확인한다.
    // 패턴 끝에 도달한 경우: 문자열도 끝났어야 함.
    if (w == W.size()) return ret = (s == S.size());
    // *를 만나서 끝난 경우: *에 몇 글자를 대응해야 할지 재귀 호출하면서 확인한다.
    // 매 단계에서 *에 아무 글자도 대응시키지 않을 것인지, 아니면 한 글자를 더 대응시킬 것인지 결정한다.
    if (W[w] == '*')
        if (matchMemoized(w+1, s) ||
            (s < S.size() && matchMemoized(w, s+1)))
            return ret = 1;
    // 이 외의 경우에는 모두 대응되지 않는다.
    return ret = 0;
}

int main() {
    // memset 을 이용해 cache 배열을 -1로 초기화 한다.
    memset(cache, -1, sizeof(cache));
    // C: 테스트 케이스의 수(1 <= C <= 10)
    // N: 파일명의 수 (1 <= N <= 50)
    int C, N;
    // 테스트 케이스의 수를 입력 받는다.
    cin >> C;
    for (int i = 0; i < C; i++) {
        // 패턴과 파일명의 수를 차례로 입력 받는다.
        cin >> W >> N;
        // N번 동안 파일명 S를 입력 받고 matchMemoized 함수를 호출한다.
        // 패턴과 파일명이 일치하면 answer 에 추가하고 cache 를 -1로 초기화한다.
        for (int j = 0; j < N; j++) {
            cin >> S;
            if (matchMemoized(0, 0))
                answer.push_back(S);
            memset(cache, -1, sizeof(cache));
        }
        // 각 테스트 케이스가 끝나면 아스키 코드 순서대로 출력하고 answer 를 초기화한다.
        sort(answer.begin(), answer.end());
        vector<string>::iterator it;
        for (it = answer.begin(); it != answer.end(); it++)
            cout << *it << endl;
        answer.clear();
    }
}