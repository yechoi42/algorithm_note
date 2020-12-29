import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a],append((b, c))

"""
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # 연결된 노드의 최단 거리 세팅
    for j in graph[start]:
        distance[j[0]] = j[1] 
    for i in range(n - 1):
        # 방문하지 않은 노드들 중에서 최단 거리가 가장 짧은 노드 꺼내기
        # = 방문하지 않았으며 distance가 INF가 아닌 것 중 짧은 노드 = 연결된 노드 중 가장 짧은 노드 꺼내기 
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 짧은 경우 최단거리 갱신ㄴ
            if cost < distance[j[0]]:
                distance[j[0]] = cost
"""              

#dijkstra using queue
def dijkstra(start):
    q = []
    heapq.heappush(q,  (0, start))
    distance[start]= 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우
    else:
        print(distance[i])
