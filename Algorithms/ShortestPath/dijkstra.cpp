//
// Created by Sujin Kim on 21. 3. 16..
//
#include <vector>
#include <queue>
#include <iostream>
#define MAX_V 100
#define INF 987654321

using namespace std;

// 정점의 개수
int V;
// 그래프의 인접 리스트 (연결된 정점 번호, 간선 가중치) 쌍을 담는다.
vector<pair<int, int> > adj[MAX_V];

// 각 정점까지의 최단 거리를 구한다.
// s = 시작 정점
vector<int> dijkstra(int s) {
    // 각 정점까지의 최단 거리를 저장하는 배열
    // 처음엔 모든 정점까지의 최단 거리를 INF 로 설정한다.
    vector<int> dist(V, INF);
    dist[s] = 0;  // w(s, s) = 0

    // (간선 가중치, 연결된 정점의 번호)
    // pair 를 비교할 때는 첫 번째 원소를 먼저 비교하므로 정점까지의 거리를 첫 번째 원소로 설정한다.
    priority_queue<pair<int, int> > pq;
    pq.push(make_pair(0, s));

    while (!pq.empty()) {
        // priority_queue 는 가장 큰 원소가 위로 가도록 구성하므로, 거리의 부호를 바꿔서 거리가 작은 정점부터 꺼내지도록 한다.
        int cost = -pq.top().first;
        int here = pq.top().second;
        pq.pop();

        // 원소를 꺼냈는데 dist[u]가 cost 보다 작다면 이 원소는 중복으로 들어간 원소이므로 무시하고 다음 원소를 꺼낸다.
        if (dist[here] < cost) continue;

        // 인접한 정점들을 모두 검사한다.
        // 이전까지 가장 짧은 경로가 a, 현재 더 짧은 경로 b를 찾았을 경우
        // 우선순위 큐에서 (a, c)를 찾아내 (b, c)로 바꾸는 대신,
        // (a, c)는 그대로 두고 (b, c)를 추가한 뒤, 나중에 큐에서 (a, c)가 꺼내지면 무시한다.
        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            int nextDist = cost + adj[here][i].second;

            // 더 짧은 경로를 발견하면, dist[]를 갱신하고 우선순위 큐에 넣는다.
            if (dist[there] > nextDist) {
                dist[there] = nextDist;
                pq.push(make_pair(-nextDist, there));
            }
        }
    }

    return dist;
}


int main() {
    V = 7;

    // adj 설정
    adj[0].emplace_back(make_pair(1, 5));
    adj[0].emplace_back(make_pair(2, 1));

    adj[1].emplace_back(make_pair(0, 5));
    adj[1].emplace_back(make_pair(3, 1));
    adj[1].emplace_back(make_pair(5, 3));
    adj[1].emplace_back(make_pair(6, 3));

    adj[2].emplace_back(make_pair(0, 1));
    adj[2].emplace_back(make_pair(3, 2));

    adj[3].emplace_back(make_pair(1, 1));
    adj[3].emplace_back(make_pair(2, 2));
    adj[3].emplace_back(make_pair(4, 5));
    adj[3].emplace_back(make_pair(5, 3));

    adj[4].emplace_back(make_pair(3, 5));

    adj[5].emplace_back(make_pair(1, 3));
    adj[5].emplace_back(make_pair(3, 5));
    adj[5].emplace_back(make_pair(6, 2));

    adj[6].emplace_back(make_pair(1, 3));
    adj[6].emplace_back(make_pair(5, 2));

    vector<int> dist = dijkstra(0);
    for (auto& d: dist) {
        cout << d << " ";
    }
}
