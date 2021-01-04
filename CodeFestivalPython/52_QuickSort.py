"""
퀵 정렬을 완성해주세요.
"""

def quick_sort(data):
    length = len(data)
    if length <= 1:
        return data
    pivot = data.pop(length // 2)
    left = []
    right = []

    for i in range(length - 1):
        left.append(data[i]) if data[i] <= pivot else right.append(data[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    input_data = map(int, input().split())
    print(quick_sort(input_data))

