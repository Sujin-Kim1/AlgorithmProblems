"""
LRU 알고리즘이란 페이지 교체 알고리즘으로써, Least Recently Used 의 약자입니다.
즉 페이지 부재가 발생했을 경우 가장 오랫동안 사용되지 않은 페이지를 제거하는 알고리즘입니다.
이 알고리즘의 기본 가설은 가장 오랫동안 이용되지 않은 페이지는 앞으로도 사용할 확률이 적다는 가정하에 페이지 교체가 진행됩니다.

메모리의 크기가 i로 주어지고 들어올 페이지들이 n으로 주어졌을 때, 전체 실행시간을 구해주세요.

만약 스택 안에 같은 스케줄이 있다면 **hit** 이라고 하며 실행시간은 **1초** 입니다.
스택 안에 스케줄이 없다면 **miss** 라고 하며 실행시간은 **6초** 입니다.

페이지             | 페이지 프레임  | 실행시간
=======================================
BCBAEBCE         | 3           | 33
ABCABCABC        | 3           | 24
ABCEDF           | 0           | 36


- 예제 1번을 보면 페이지 프레임의 개수는 3개이고 스케줄은 'BCBAEBCE' 입니다.
5번의 miss 를 기록하므로 '5번 * 6초 = 30초' 가 되고  3번의 hit 을 기록하므로 '3번 * 1초 = 3초' 입니다.
2개를 합한 값이 실행시간이므로, 33초가 됩니다.
"""


# 방금 사용한 프레임의 used_time 은 0으로 표시하고, 나머지는 -1을 해준다
def calculate_used_time(used_time, used_idx):
    for t in range(len(used_time)):
        used_time[t] = 0 if t == used_idx else used_time[t] - 1
    return used_time


# LRU 페이지 교체 알고리즘에 따라 실행 시간이 얼마나 걸리는지 반환한다.
def page_fault_LRU(page, frame):
    # 페이지 프레임이 0이라면 모든 페이지마다 페이지 교체가 발생한다.
    if frame == 0:
        return len(page) * 6

    # 사용 시간을 나타내는 리스트를 페이지 프레임의 크기만큼 초기화 한다.
    # 방금 사용한 프레임은 0으로 표시하고, 사용하지 않을 때마다 -1을 해준다.
    # 가장 낮은 수를 가진 인덱스는 가장 오랫동안 이용되지 않았음을 의미하므로 페이지 교체 인덱스가 된다.
    used_time = [9999] * frame
    memory = []  # page 를 저장하는 메모리
    total_time = 0  # 전체 실행 시간
    for p in page:
        # hit
        if p in memory:
            total_time += 1
        # miss
        else:
            # 메모리가 다 차지 않은 경우
            if len(memory) < frame:
                memory.append(p)
            # 메모리가 다 찬 경우, 가장 오랫동안 이용되지 않아 used_time 가 최소인 값을 인덱스로 하는 값으로 페이지 교체 발생
            else:
                memory.pop(used_time.index(min(used_time)))
                memory.append(p)
            # miss 일 경우 메모리 크기와 관계 없이 6초의 실행 시간이 걸린다.
            total_time += 6

        # 가장 최근에 사용한 프레임의 시간은 0으로, 나머지는 -1
        used_time = calculate_used_time(used_time, memory.index(p))
    return total_time


# 가장 오랫동안 이용되지 않은 페이지가 앞에 오도록 메모리 설정
def refactoring_LRU(page, frame):
    # 페이지 프레임이 0이라면 모든 페이지마다 페이지 교체가 발생한다.
    if frame == 0:
        return len(page) * 6

    memory = []  # page 를 저장하는 메모리. 인덱스가 클수록 가장 최근에 사용함.
    total_time = 0  # 전체 실행 시간
    for p in page:
        # hit
        if p in memory:
            # 가장 최근에 사용한 페이지를 제일 뒤에 오도록 설정
            memory.append(memory.pop(0))
            total_time += 1
        # miss
        else:
            # 메모리가 다 차지 않은 경우
            if len(memory) < frame:
                memory.append(p)
            # 메모리가 다 찬 경우, 가장 오랫동안 이용되지 않은 페이지를 교체한다.
            else:
                memory = memory[1:] + [p]
            # miss 일 경우 메모리 크기와 관계 없이 6초의 실행 시간이 걸린다.
            total_time += 6
    return total_time


if __name__ == '__main__':
    executions = [('BCBAEBCE', 3), ('ABCABCABC', 3), ('ABCEDF', 0)]
    for execution in executions:
        print(page_fault_LRU(execution[0], execution[1]))
    print()
    for execution in executions:
        print(refactoring_LRU(execution[0], execution[1]))
