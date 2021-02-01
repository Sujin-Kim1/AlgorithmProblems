"""
토끼들이 징검다리를 건너려고 합니다. 하지만 돌이 부실해서 몇번 건너지 못할것 같습니다.
대기중인 토끼들의 통과 여부를 배열에 담아 출력해주세요

1. 각 돌들이 얼마나 버틸수 있는지 배열로 주어집니다.

2. 각 토끼가 착지할때 마다 돌의 내구도는 1씩 줄어듭니다.
    ex) [1,2,1,4] 각 돌마다 1마리 2마리 1마리 4마리의 착지를 버틸 수 있습니다.

3. 토끼들은 점프력이 각자 다릅니다.
    ex)[2,1] 첫번째 토끼는 2칸씩 두번째 토끼는 1칸씩 점프합니다.

4. 각 토끼들은 순서로 다리를 건넙니다.

**입력**
돌의내구도 = [1, 2, 1, 4]
토끼의점프력 = [2, 1]

**출력**
['pass', 'pass']

**입력**
돌의내구도 = [1, 2, 1, 4, 5, 2]
토끼의점프력 = [2, 1, 3, 1]

**출력**
['pass', 'pass', 'fail', 'fail']
"""


# 각 토끼들이 돌을 통과할 수 있으면 'pass', 통과할 수 없으면 'fail' 을 담은 리스트 반환
def the_march_of_rabbits(durability, jump_power):
    # 통과 여부를 저장하는 리스트
    # 초기 설정은 모두 'pass' 로 설정
    result = ['pass'] * len(jump_power)
    for power_idx in range(len(jump_power)):
        # 점프력만큼 뛴다.
        for durability_idx in range(jump_power[power_idx] - 1, len(durability), jump_power[power_idx]):
            # 토끼가 착지할 때마다 돌의 내구도는 1씩 줄어든다.
            durability[durability_idx] -= 1
            # 내구도가 0보다 작으면 건널 수 없으므로 fail 을 저장하고 다음 순환으로 넘어간다.
            if durability[durability_idx] < 0:
                result[power_idx] = 'fail'
    return result


if __name__ == '__main__':
    d = list(map(int, input('돌의 내구도: ').split()))
    j = list(map(int, input('토끼의 점프력: ').split()))
    print(the_march_of_rabbits(d, j))
