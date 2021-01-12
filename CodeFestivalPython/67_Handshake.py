"""
광장에서 모인 사람들과 악수를 하는 행사가 열렸다.
참가자인 민규는 몇명의 사람들과 악수를 한 후 중간에 일이 생겨 집으로 갔다.
이 행사에서 진행된 악수는 총 n번이라고 했을때.

민규는 몇번의 악수를 하고 집으로 돌아갔을까?
이때 민규를 포함한 행사 참가자는 몇명일까?

- 악수는 모두 1대 1로 진행이 된다.
- 민규를 제외한 모든 참가자는 자신을 제외한 참가자와 모두 한번씩 악수를 한다.
- 같은 상대와 중복된 악수는 카운트 하지 않는다.
- 민규를 제외한 참가자는 행사를 모두 마쳤다.

input : n (행사에서 진행된 악수 횟수)
output : [ 민규의 악수횟수 , 행사참가자 ]
예) solution(59) = [4, 12]
설명)
59회의 악수가 행사에서 진행되었다.
이때 민규는 4번의 악수를 하였고 민규를 포함한 참가자는 12명이다.
"""


def handshake(n):
    participants = 0
    handshaking_num = 0
    while True:
        participants += 1
        if n <= handshaking_num + participants:
            break
        handshaking_num += participants

    return [n - handshaking_num, participants + 1]


def another_solution(n):
    people = 0
    total = 0
    while True:
        total = people * (people - 1) // 2
        if n < total:
            break
        people += 1
    times = int(people - (total - n) - 1)
    return [times, people]


if __name__ == '__main__':
    print(handshake(int(input())))
