"""
문자열을 입력받고 연속되는 문자열을 압축해서 표현하고싶습니다.

**입력**
aaabbbbcdddd

**출력**
a3b4c1d4

# 정규 표현식
# . ^ $ { } [ ] ( ) ₩ | *
# [a-zA-Z] - 알파벳 모두
# ₩d       - 숫자
# ₩s       - 문자
# ₩w       - 문자와 숫자를 매칭
# ₩W       - 문자와 숫자가 아닌 것을 매칭 [^a-zA-Z0-9]
# *, +     - 반복
# match    - 매치를 위해 검색하는 수행하는 string 메소드. 배열 또는 null 문자 반환. 지정된 패턴과 동일한 패턴을 찾는다.
# search   - 문자열이 있는지 검사하는 string 메소드. 대응되는 문자열의 인덱스 반환 (없으면 -1).
# findall  - 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer - 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

"""


# my solution
def string_compression(s):
    if len(s) == 0:
        return

    count = 0
    base = s[0]
    answer = ''
    for i in s:
        if i != base:
            answer += base + str(count)
            count = 1
            base = i
        else:
            count += 1
    answer += base + str(count)
    print(answer)


import re


# example for understanding
def example(input_data):
    rule = re.compile('[a-c]+')

    one = re.findall('b', input_data)  # find all 'b's.
    two = re.findall(rule, input_data)  # find repeated 'a' ~ 'c'.
    three = re.findall('(\\w)(\\1*)', input_data)  # find a word and string that repeats more than one.

    print(one)
    print(two)
    print(three)


# answer 2
def answer2(input_data):
    one = re.findall('(\\w)(\\1*)', input_data)

    s = ''
    for i, j in one:
        s += i + str(len(j) + 1)
    print(s)


if __name__ == '__main__':
    s = input()
    string_compression(s)
    example(s)
    answer2(s)
