"""
천하 제일 먹기 대회가 개최되었습니다.
이 대회는 정해진 시간이 끝난 후 음식을 먹은 그릇 개수를 파악한 후 각 선수들의 등수를 매깁니다.

1. 같은 이름의 선수는 없습니다.
2. 접시의 수가 같은 경우는 없습니다.

**입력 예1)**
손오공 야모챠 메지터 비콜로
70 10 55 40

**출력 예1)**
{'손오공': 1, '메지터': 2, '비콜로': 3, '야모챠': 4}

**입력 예2)**
["홍길동","엄석대","연개소문","김첨지"]
[2, 1, 10, 0]

**출력 예2)**
{'연개소문': 1, '홍길동': 2, '엄석대': 3, '김첨지': 4}
"""


def food_fight(names, plates):
    li = sorted(list(zip(names, plates)), key=lambda x: x[1], reverse=True)
    answer = {}
    for idx, key in enumerate(li):
        answer[key[0]] = idx + 1
    return answer


if __name__ == '__main__':
    n = input().split()
    p = list(map(int, input().split()))
    print(food_fight(n, p))
