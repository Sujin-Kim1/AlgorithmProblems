"""
호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다. 호준이가 일하는 학원은 매번 1위부터 3위까지의 학생에게 상으로 사탕을 준다.
그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고 점수를 보내면, 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.

학생들의 점수를 공백으로 구분하여 입력받는다. 1위~ 3위 학생은 여러명일 수 있고 1~3위 학생 중 중복되는 학생까지 포함하여 사탕을 사기로 한다.

```
점수입력 : 97 86 75 66 55 97 85 97 97 95
출력 : 6
```
"""


def needed_candy(li):
    sorted_li = sorted(li, reverse=True)
    winner = sorted_li[0]  # max score
    count = third_count = 0

    for item in sorted_li:
        if winner != item:
            winner = item
            third_count += 1
        if third_count == 3:
            break
        count += 1

    print(count)


if __name__ == '__main__':
    scores = input().split()
    needed_candy(scores)
