"""
수학공식이 제대로 입력이 되었는지 판단하는 코드를 작성하려 합니다.

**입출력 예시**
데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + 7 * {(3 * 5)}
True

데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + 7){ * (3 * 5)
False

데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + (7 * {3 * 5})
False

데이터 입력(1), 프로그램 종료(2) : 2
"""


def math(ex):
    parentheses = {'[': ']', '{': '}', '(': ')'}
    # 괄호의 우선순위(인덱스가 클수록 우선순위가 높음)
    priority = '({['
    # 괄호를 담을 스택
    stack = []

    for e in ex:
        # (, {, [ 일 경우
        # 우선순위를 파악하여 스택에 추가
        if e in parentheses.keys():
            # 우선순위가 더 높은 괄호가 있을 경우 False
            if len(stack) > 0 and priority.index(stack[-1]) < priority.index(e):
                return False
            # 그렇지 않으면 stack 에 괄호 추가
            stack.append(e)

        # ), }, ] 일 경우
        elif e in parentheses.values():
            # stack 이 비어 있거나 쌍이 안맞으면 false 반환
            if len(stack) == 0 or e != parentheses[stack[-1]]:
                return False
            # 그렇지 않으면 stack 에서 마지막 원소 삭제
            stack.pop()
    # 스택이 비어있을 경우 참
    return len(stack) == 0


if __name__ == '__main__':
    while 1:
        order = input('데이터 입력(1), 프로그램 종료(2) :')
        if order == '1':
            example = input('데이터를 입력하세요 :')
            print(math(example))
        else:
            break
