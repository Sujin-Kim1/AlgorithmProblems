"""
**조합**이란 원소들을 조합하여 만들 수 있는 경우의 수이며 원소의 순서는 신경쓰지 않습니다.
**순열**이란 원소의 값이 같더라도 순서가 다르면 서로 다른 원소로 취급하는 선택법입니다.

한글의 자모 24자 중 자음은 총 14개 입니다.
이 중 입력받은 자음을 n개를 선택하여 나올 수 있는 모든 조합과, 조합의 수를 출력하고 싶습니다.

‘한글 맞춤법’의 제2장 제4항에서는 한글의 기본 자모 24자
“ㄱ(기역), ㄴ(니은), ㄷ(디귿), ㄹ(리을), ㅁ(미음), ㅂ(비읍), ㅅ(시옷),
ㅇ(이응), ㅈ(지읒), ㅊ(치읓), ㅋ(키읔), ㅌ(티읕), ㅍ(피읖), ㅎ(히읗),
ㅏ(아), ㅑ(야), ㅓ(어), ㅕ(여), ㅗ(오), ㅛ(요), ㅜ(우), ㅠ(유), ㅡ(으), ㅣ(이)”를 제시

나올 수 있는 모든 조합을 아래와 같이 출력해주세요.

**<--요구조건-->**
1. 첫 줄에 선택할 한글 자음이 주어집니다.
2. 두번째 줄에 조합의 수가 주어집니다.
3. 주어진 조합의 수에 따라 조합과 조합의 수를 출력해주세요.

**입력**
ㄱ,ㄴ,ㄷ,ㄹ
3

**출력**
['ㄱㄴㄷ', 'ㄱㄴㄹ', 'ㄱㄷㄹ', 'ㄴㄷㄹ']
4
"""

answer = []


# n: 전체 원소들의 수
# to_pick: 더 골라야 할 원소들의 개수
# picked: 지금까지 고른 원소들의 번호
# hangul: 입력 받은 한글 자음의 리스트
# 일 때, 앞으로 to_pick 개의 원소를 고르는 모든 방법을 answer 에 저장한다.
def pick(n, to_pick, picked, hangul):
    # 기저 사례: 더 고를 원소 X
    if to_pick == 0:
        return answer.append("".join(picked))
    # 고를 수 있는 가장 작은 인덱스 찾기
    smallest = 0 if len(picked) == 0 else hangul.index(picked[-1]) + 1
    # 원소 하나를 고른다.
    for next_element in range(smallest, n):
        picked.append(hangul[next_element])
        pick(n, to_pick - 1, picked, hangul)
        picked.pop()


# 라이브러리를 사용하는 방법
from itertools import combinations


def another_solution(hangul, n):
    result = list(map(''.join, combinations(hangul, n)))
    print(result, len(result))


if __name__ == '__main__':
    hangul = list(input().split())
    n = int(input())
    picked = []
    pick(len(hangul), n, picked, hangul)
    print(answer, len(answer))
    another_solution(hangul, n)
