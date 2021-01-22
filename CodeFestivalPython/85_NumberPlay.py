"""
일정한 규칙을 가지고있는 숫자를 나열하는 놀이를 하는 중입니다.
이전 숫자에서 각 숫자의 갯수를 나타내어 숫자로 만들고 다시 그 숫자를 같은 규칙으로 만들며 나열 합니다.
이 놀이는 1부터 시작합니다.
다음수는 1이 1개 이기때문에 '11'이 되고
 '11'에서 1이 2개이기때문에 그 다음은 '12'가 됩니다.

즉,
1. 1  → (1)
2. 11 → (1이 1개)
3. 12 → (1이 2개)
4. 1121 → (1이 1개 2가 1개)
5. 1321 → (1이 3개 2가 1개)
6. 122131 → (1이 2개 2가 1개 3이 1개)
7. 132231 → (1이 3개 2가 2개 3이 1개)

위와 같이 진행되는 규칙을 통해
진행횟수 N을 입력받으면 해당되는 수를 출력하세요.

**입력**
6

**출력**
122131
"""


def number_play(n):
    answer = '1'

    for count in range(1, n):
        # answer 에서 각 숫자와 숫자의 개수를 저장하는 dictionary
        answer_dic = {}
        for i in answer:
            answer_dic[i] = answer.count(i)
        # 각 숫자와 그 숫자의 개수를 리스트로 저장한다. (숫자를 기준으로 오름차순 정렬)
        answer_li = sorted(list(answer_dic.items()))
        answer = ''.join(number + str(number_count) for number, number_count in answer_li)
    return answer


def another_solution(n):
    answer = '1'
    for i in range(1, n):
        answer = rule(answer)
        print(answer)
    return answer


def rule(n):
    num_l = max([int(i) for i in n])
    d = [str(i) + str(str(n).count(str(i))) for i in range(1, num_l + 1)]
    return ''.join(d)


if __name__ == '__main__':
    print(number_play(int(input())))
    print(another_solution(int(input())))
