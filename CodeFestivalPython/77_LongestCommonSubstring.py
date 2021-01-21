"""
**가장 긴 공통 부분 문자열(Longest Common Subsequence)**이란 A, B 두 문자열이 주어졌을 때
두 열에 공통으로 들어 있는 요소로 만들 수 있는 가장 긴 부분열을 말합니다.
여기서 부분열이란 다른 문자열에서 몇몇의 문자가 빠져 있어도 순서가 바뀌지 않은 열을 말합니다.

예를 들어
S1 = ['T', 'H', 'E', 'S', 'T', 'R', 'I', 'N', 'G', 'S']
S2 = ['T', 'H', 'I', 'S', 'I', 'S']
라는 두 문자열이 있을 때 둘 사이의 부분 공통 문자열의 길이는
['T', 'H', 'S', 'T', 'I', 'S'] 의 6개가 됩니다.

이처럼 **두 문자열이 주어지면 가장 긴 부분 공통 문자열의 길이를 반환하는 프로그램**을 만들어 주세요.

두 개의 문자열이 한 줄에 하나씩 주어집니다.
문자열은 알파벳 대문자로만 구성되며 그 길이는 100글자가 넘어가지 않습니다.

출력은 이 두 문자열의 가장 긴 부분 공통 문자열의 길이를 반환하면 됩니다.

**- Test Case -**

**입력**
THISISSTRINGS
THISIS

**출력**
6

-

**입력**
THISISSTRINGS
TATHISISKKQQAEW

**출력**
6

-

**입력**
THISISSTRINGS
KIOTHIKESSISKKQQAEW

**출력**
3

-

**입력**
THISISSTRINGS
TKHKIKSIS

**출력**
3
"""


def longest_common_substring(s1, s2):
    # 공통 부분 문자열의 길이
    common_string_count = 0
    # 길이가 짧은 문자열이 s2가 되도록 설정
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    # 공통 길이는 s2를 기준으로 계산한다.
    # s2의 부분 문자열의 길이를 하나씩 늘려가면서 s1에 s2의 부분 문자열이 존재하는지 판단한다.
    for length in range(1, len(s2) + 1):
        for pos in range(len(s2) - length + 1):
            # 부분 문자열이 존재하면 common_string_count 를 증가하고 length 를 늘려 다시 판단한다.
            if s2[pos:pos + length] in s1:
                common_string_count += 1
                break
            # length 가 가장 긴 부분 문자열의 길이가 아닌 경우 common_string_count 를 반환한다.
            if pos == len(s2) - length and s2[pos:pos + length] not in s1:
                return common_string_count
    return common_string_count


""" 
list 의 내장 함수를 이용한 방법
"""
# 부분 문자열의 모든 경우의 수를 구한다.
def determines_listed_string_number(s):
    result = []
    for i in range(1, len(s) + 1):
        for j in range(i):
            result.append(s[j:j + len(s) - i + 1])
    return result


def longest_common_substring_using_library(s1, s2):
    s1_list = set(determines_listed_string_number(s1))
    s2_list = set(determines_listed_string_number(s2))
    # 경우의 수 교집합
    answers = s1_list.intersection(s2_list)
    # 가장 긴 교집합
    answer = max(answers, key=len)
    return len(answer)


if __name__ == '__main__':
    test_num = int(input())
    for test in range(test_num):
        S1 = input()
        S2 = input()
        print(longest_common_substring(S1, S2))
        print(longest_common_substring_using_library(S1, S2))
