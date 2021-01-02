"""
진구는 영어 학원 아르바이트를 하고 있습니다. 반 아이들은 알파벳을 공부하는 학생들인데 오늘은 대문자 쓰기 시험을 봤습니다.

알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES를 아니면 NO를 출력하는 프로그램을 만들어 주세요.

→ 알파벳 여러개를 입력하고 여러개 입력한 것 중 대문자만 출력해주는 프로그램도 만들어보세요.
"""


def is_upper_case(alphabet):
    print('YES' if alphabet.isupper() else 'NO')


def print_only_upper_case(string):
    for s in string:
        if s.isupper():
            print(s, end='')


if __name__ == '__main__':
    a = input('alphabet: ')
    s = input('string: ')
    is_upper_case(a)
    print_only_upper_case(s)
