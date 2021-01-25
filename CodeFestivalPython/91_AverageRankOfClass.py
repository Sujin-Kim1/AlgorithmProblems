"""
한 반에 30명인 학생, 총 7개의 반 점수가 '국어, 영어, 수학, 사회, 과학' 순서로 있는 다중 리스트를 랜덤한 값으로 만들어주시고 아래 값을 모두 출력하세요.

1. 반 점수 모두가 담긴 전교 점수 다중 리스트를 만들어주세요.
2. 반 평균을 구하세요.
3. 반 1등 점수를 구하세요.
4. 전교 평균을 구하세요.

(출력 형식은 상관 없습니다.)

- numpy 를 사용해서도 풀어보세요.
"""

import numpy as np
import random as r


def average_rank_of_class():
    score = []  # 5과목
    class_score = []  # 한 반에 30명
    total_score = []  # 총 7개의 반

    total = 0  # 점수의 총합
    for t in range(7):
        for c in range(30):
            for s in range(5):
                score.append(r.randint(1, 100))
            class_score.append(score)
            total += sum(score)
            score = []  # 한 사람의 점수를 class_score 에 추가한 후, 빈 리스트로 초기화
        total_score.append(class_score)
        class_score = []  # 한 반의 점수를 total_score 에 추가한 후, 빈 리스트로 초기화

    average = total / (len(total_score) * len(total_score[0]) * len(total_score[0][0]))
    print(average)


def average_rank_of_class_using_numpy():
    print(np.average(np.random.random_sample((7, 30, 5)) * 100))


if __name__ == '__main__':
    average_rank_of_class()
    average_rank_of_class_using_numpy()
