"""
다음의 딕셔너리가 주어졌을 때 주어진 나라의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

**데이터**
nationWidth = {
     'Korea': 220877,
     'Russia': 17098242,
     'China': 9596961,
     'France': 543965,
     'Japan': 377915,
     'England' : 242900 }

**출력**
England 22023
"""


def closest_nation(d, nation):
    result = []

    # dictionary to list sorted by width in ascending order
    nation_list = sorted(list(d.items()), key=lambda x: x[1])

    # find country with the closest area
    for i in range(len(nation_list)):
        if nation_list[i][0] == nation:
            # smallest nation
            if i == 0:
                result = [nation_list[i + 1][0], nation_list[i + 1][1] - nation_list[i][1]]
                break
            # biggest nation
            if i == len(nation_list) - 1:
                result = [nation_list[i - 1][0], nation_list[i][1] - nation_list[i - 1][1]]
                break
            # select nation of similar area
            if (nation_list[i][1] - nation_list[i - 1][1]) < (nation_list[i + 1][1] - nation_list[i][1]):
                result = [nation_list[i - 1][0], nation_list[i][1] - nation_list[i - 1][1]]
                break
            else:
                result = [nation_list[i + 1][0], nation_list[i + 1][1] - nation_list[i][1]]
                break
    return print(result[0], result[1])


def answer(nation_width_d, nation):
    w = nation_width_d[nation]
    nation_width_d.pop(nation)
    l = list(nation_width_d.items())
    gap = max(nation_width_d.values())
    item = 0

    for i in l:
        if gap > abs(i[1] - w):
            gap = abs(i[1] - w)
            item = i
    print(item[0], abs(item[1] - w))


if __name__ == '__main__':
    nation_width = {'Korea': 220877, 'Russia': 17098242, 'China': 9596961,
                   'France': 543965, 'Japan': 377915, 'England': 242900}
    closest_nation(nation_width, input())
    answer(nation_width, input())
