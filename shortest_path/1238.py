import sys
import heapq
import copy

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[e].append((s, t))

def dijkstra(start, n):
    distance = [INF] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance

dist_to_x = dijkstra(x, n)

answer = 0
for i in range(1, n + 1):
    if dist_to_x[i] == INF:
        dist_to_x[i] = 0
    dist_to_home = dijkstra(i, n)
    answer = max(answer, dist_to_home[x] + dist_to_x[i])

print(answer)