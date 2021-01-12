"""
다음과 같이 노드의 연결 관계가 그래프 형태로 주어집니다. 그 다음 경로를 구할 두 정점이 공백으로 구분되어 주어질 것입니다.

두 정점 사이를 이동할 수 있는 최단거리를 출력하는 프로그램을 작성해 주세요.

이 때 최단 거리란, 정점의 중복 없이 한 정점에서 다른 정점까지 갈 수 있는 가장 적은 간선의 수를 의미합니다.

**데이터**
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E', 'G'])}
         'G': set(['F'])}

**입출력**

입력 : A G
출력 : 3
"""

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'H'},
    'D': {'B', 'H'},
    'E': {'B', 'F'},
    'F': {'C', 'E', 'G'},
    'G': {'F'},
    'H': {'C', 'D'}
}


# initialize the distance of the rest of the nodes to 999
def initialize_distance(start):
    distance = {}
    for node in graph:
        distance[node] = 999 if node != start else 0
    return distance


# find min distance
def extract_min(d, q, n):
    for i in q:
        if d[n] + 1 < d[i]:
            d[i] = d[n] + 1
    return d


# find all of shortest path distance (start -> destination)
# if you return when destination is in temp, you can find shortest path more quickly.
def shortest_path(start, destination):
    distance = initialize_distance(start)
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            temp = graph[n] - set(visited) - set(queue)
            queue += temp
            if len(temp) > 0:
                distance = extract_min(distance, queue, n)
        # print('node:', n)
        # print('    visited:', visited)
        # print('    queue:', queue)
        # print('    distance:', distance)
    return distance[destination]


# there is no weight, so height of BFS is shortest path
def another_solution(start, end):
    queue = [start]
    visited = [start]

    count = -1

    while queue:
        count += 1
        size = len(queue)
        # print(f'count = {count}')
        for i in range(size):
            node = queue.pop(0)
            # print(f'    node = {node}')
            if node == end:
                return count

            for next_node in graph[node]:
                # print(f'        graph[node] = {graph[node]}')
                # print(f'        next_node = {next_node}')
                if next_node not in visited:
                    queue.append(next_node)
                    visited.append(next_node)
                    # print(f'            visited = {visited}')
                    # print(f'            queue = {queue}')

    return count


if __name__ == '__main__':
    print(shortest_path('A', 'H'))
    print('----------------------------------------------')
    print(another_solution('A', 'H'))
