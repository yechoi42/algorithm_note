import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [INF] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(X)

answer=[]
for i in range(1, N + 1):
    if distance[i] == K:
        answer.append(i)

if len(answer):
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)