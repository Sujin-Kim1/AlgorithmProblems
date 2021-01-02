"""
버블정렬은 두 인접한 원소를 검사하여 정렬하는 방법을 말합니다.
시간 복잡도는 느리지만 코드가 단순하기 때문에 자주 사용됩니다.

버블 정렬을 작성해 봅시다.
"""

def bubble_sort(n, data):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    for i in data:
        print(i, end=' ')


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    bubble_sort(n, data)
