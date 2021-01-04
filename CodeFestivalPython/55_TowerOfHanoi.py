"""
하노이의 탑은 프랑스 수학자 에두아르드가 처음으로 발표한 게임입니다. 하노이의 탑은 A, B, C 3개의 기둥과 기둥에 꽂을 수 있는 N개의 원판으로 이루어져 있습니다. 이 게임에서 다음의 규칙을 만족해야 합니다.

1. 처음에 모든 원판은 A기둥에 꽂혀 있다.
2. 모든 원판의 지름은 다르다.
3. 이 원반은 세 개의 기둥 중 하나에 반드시 꽂혀야 한다.
4. 작은 원반 위에 큰 원반을 놓을 수 없다.
5. 한 번에 하나의 원판(가장 위에 있는 원판) 만을 옮길 수 있다.

이 규칙을 만족하며 A기둥에 있는 원반 N개를 모두 C 원반으로 옮기고 싶습니다.
모든 원반을 옮기기 위해 실행되어야 할 최소 원반 이동 횟수를 계산하는 프로그램을 완성해주세요.
"""

def move(n, start, to):
    print("Disk {} moved from {} to {}".format(n, start, to))


def tower_of_hanoi(N, start, to, via):
    if N == 1:
        move(N, start, to)
    else:
        tower_of_hanoi(N - 1, start, via, to)
        move(N, start, to)
        tower_of_hanoi(N - 1, via, to, start)


if __name__ == '__main__':
    tower_of_hanoi(3, 'A', 'C', 'B')
