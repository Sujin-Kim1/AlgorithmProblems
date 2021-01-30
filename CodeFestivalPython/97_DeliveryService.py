"""
n명의 택배 배달원은 쌓인 택배를 배달해야 합니다.
각 택배는 접수된 순서로 배달이 되며 택배 마다 거리가 주어집니다.
거리1당 1의 시간이 걸린다고 가정하였을 때 모든 택배가 배달 완료될 시간을 구하세요.

1. 모든 택배의 배송 시간 1 이상이며 배달지에 도착하고 돌아오는 왕복시간입니다.
2. 택배는 물류창고에서 출발합니다.
3. 배달을 완료하면 다시 물류창고로 돌아가 택배를 받습니다.
4. 물류창고로 돌아가 택배를 받으면 배달을 시작합니다.
5. 택배를 상차 할 때 시간은 걸리지 않습니다.

입력은 배달원의 수와 택배를 배달하는 배달 시간이 주어집니다.

ex) 배달원이 3명이고 각 거리가 [1,2,1,3,3,3]인 순서로 들어오는 경우

# 입력값
배달원 = 3
배달시간 = [1,2,1,3,3,3]

# 출력값 = 5

배달원1    배달원2     배달원3    시간
===================================
  1        2         1      택배 상차
  0        1         0      1초 경과
  3        1         3      택배 상차
  2        0         2      1초 경과
  2        3         2      택배 상차
  1        2         1      1초 경과
  0        1         0      1초 경과
  0        0         0      1초 경과 - 배달 완료
"""


# n: 택배원의 수, delivery_time: 택배 거리
# 택배를 모두 배달하는데 걸리는 시간 반환
def delivery_service(n, delivery_time):
    # 총 택배 배송 시간
    total = 0
    # 택배원 수 만큼의 배열 생성
    delivery_in_progress = [0] * n
    # 모든 택배가 상차 되었을 경우 종료
    while delivery_time:
        # 택배원 수 만큼 반복
        for i in range(n):
            # 베송 완료인 경우 택배 상차
            if delivery_in_progress[i] == 0 and delivery_time:
                delivery_in_progress[i] = delivery_time.pop(0)
        # 배송 거리 - 1
        delivery_in_progress = list(map(lambda x: x - 1, delivery_in_progress))
        # 1회 반복당 시간 1 증가
        total += 1
    # 남은 택배 잔여 거리 중 가장 많이 남은 시간을 더해줌
    return total + max(delivery_in_progress)


if __name__ == '__main__':
    n = int(input('배달원: '))
    d = list(map(int, input('배달시간: ').split()))
    print(delivery_service(n, d))
