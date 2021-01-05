"""
학교가 끝난 지원이는 집에 가려고 합니다. 학교 앞에 있는 버스 시간표는 너무 복잡해서 버스 도착시간이 몇 분 남았는지 알려주는 프로그램을 만들고 싶습니다.
버스시간표와 현재 시간이 주어졌을 때 버스 도착 시간이 얼마나 남았는지 알려주는 프로그램을 만들어주세요.

- 버스 시간표와 현재시간이 입력으로 주어집니다.
- 출력 포맷은 "00시00분"입니다.
   만약 1시간 3분이 남았다면 "01시간03분"으로 출력해야 합니다.
- 버스 시간표에 현재 시간보다 이전인 버스가 있다면 "지나갔습니다."라고 출력합니다.

**입력**
["12:30", "13:20", "14:13"]
"12:40"

**출력**
['지나갔습니다', '0시간 40분', '1시간 33분']
"""


def bus_schedule(schedule, current):
    result = []
    for i in schedule:
        schedule_minutes = int(i[:2]) * 60 + int(i[3:])
        current_minutes = int(current[:2]) * 60 + int(current[3:])
        time_remaining = schedule_minutes - current_minutes
        if time_remaining < 0:
            result.append('지나갔습니다')
        else:
            hour = str(time_remaining // 60)
            minutes = str(time_remaining % 60)
            result.append(hour.zfill(2) + '시간' + minutes.zfill(2) + '분')
    print(result)


if __name__ == '__main__':
    s = ["12:30", "13:20", "14:13"]
    c = "12:40"
    bus_schedule(s, c)
