//
// Created by Sujin Kim on 21. 3. 17..
//

#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#define MAX_N 201
#define INF 1e9

using namespace std;

// 그래프의 인접 리스트 (연결된 정점 번호, 간선 가중치) 쌍을 담는다.
vector<pair<int, int> > adj[MAX_N];

// 택시 요금을 양방향으로 저장한다.
void initializeAdj(vector<vector<int>> & fares) {
    for (auto & fare : fares) {
        fare[0]--, fare[1]--;  // 인덱스가 0에서 부터 시작하므로
        adj[fare[0]].emplace_back(make_pair(fare[1], fare[2]));
        adj[fare[1]].emplace_back(make_pair(fare[0], fare[2]));
    }
}

long long dijkstra(int n, int s, int dst) {
    int result;
    // 각 정점까지의 최단 거리를 저장하는 배열
    // 처음엔 모든 정점까지의 최단 거리를 INF로 설정한다.
    vector<int> dist(n, INF);
    dist[s] = 0;  // w(s, s) = 0

    // (간선 가중치, 연결된 정점의 번호)
    // pair를 비교할 때는 첫 번째 원소를 먼저 비교하므로 정점까지의 거리를 첫 번째 원소로 설정한다.
    priority_queue<pair<int, int> > pq;
    pq.push(make_pair(0, s));

    while (!pq.empty()) {
        // min-heap을 위해 거리의 부호를 바꾼다.
        int cost = -pq.top().first;
        int here = pq.top().second;
        pq.pop();

        // 원소를 꺼냈는데 dist[here]가 cost 보다 작다면 이 원소는 중복으로 들어간 원소이므로 무시하고 다음 원소를 꺼낸다.
        if (dist[here] < cost) continue;

        // 인접한 정점들을 모두 검사한다.
        // 이전까지 가장 짧은 경로가 a, 현재 더 짧은 경로 b를 찾았을 경우
        // 우선순위 큐에서 (a, c)를 찾아내 (b, c)로 바꾸는 대신,
        // (a, c)는 그대로 두고 (b, c)를 추가한 뒤, 나중에 큐에서 (a, c)가 꺼내지면 무시한다.
        for (auto & i : adj[here]) {
            int there = i.first;
            int nextDist = cost + i.second;

            // 더 짧은 경로를 발견하면, dist[]와 parent[]를 갱신하고 우선순위 큐에 넣는다.
            if (dist[there] > nextDist) {
                dist[there] = nextDist;
                pq.push(make_pair(-nextDist, there));
            }
        }
    }
    return dist[dst];
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    long long answer = 0;
    s--, a--, b--;  // 인덱스가 0에서부터 시작하므로
    initializeAdj(fares);

    // a, b 각각의 최단 거리 비용을 먼저 구하고 더함
    answer = dijkstra(n, s, a) + dijkstra(n, s, b);
    // 특정 지점까지 합승했을 때 비용과 비교
    for (int i = 0; i < n; i++) {
        if (s != i)
            answer = min(answer, dijkstra(n, s, i) + dijkstra(n, i, a) + dijkstra(n, i, b));
    }
    return answer;
}