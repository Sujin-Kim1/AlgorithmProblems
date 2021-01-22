"""
의약품 성분이 총 8개인 약품들이 있습니다. 예를들어 다음 데이터는 총 8개의 성분을 갖습니다.

판콜비 = 'ABCDEFGH'
넥타이레놀 = 'EFGHIJKL'

특정 약품 A의 성분이 공개되었을 때, 이와 유사한 성분을 가진 데이터들의 출력을 구하는 문제입니다.

입력 : 'ABCDEFGH' 4
데이터 : 'EFGHIJKL', 'EFGHIJKM', 'EFGHIJKZ' 등 1만개의 데이터
출력 : 'EFGHIJKL', 'EFGHIJKM', 'EFGHIJKZ' 등 4개의 요소가 같은 약품 전부
      (4개 이상이 아니며 같은 요소가 4개인 것을 출력해야 합니다.)

* 해당 문제는 시간 제한이 있습니다.
* 제약 데이터의 성분은 중복이 될 수 없습니다.
(예를 들어 'AAABBBAB'와 같은 데이터는 없습니다.)
"""


import random as r



def find_same_ingredient(ingredient, n):
    # A ~ Z
    alphabets = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # 같은 의약성분의 개수가 n 과 같은 것만 추가하는 리스트
    total_medicine = []

    for i in range(10001):
        medicine = r.sample(alphabets, len(ingredient))

        # count = 0
        # for j in range(len(ingredient)):
        #     if medicine[j] in ingredient:
        #         count += 1
        # if count == n:
        #     total_medicine.append(''.join(medicine))
        #                    ↓

        if len(set(medicine) & set(ingredient)) == n:
            total_medicine.append(''.join(medicine))
    return total_medicine


if __name__ == '__main__':
    result = find_same_ingredient(input(), int(input()))
    print(result)
    print(len(result))  # 개수 출력

