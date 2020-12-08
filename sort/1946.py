import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    scores = []
    for _ in range(N):
        X, Y = map(int, sys.stdin.readline().split())
        scores.append((X, Y))
    scores.sort()
    count = 0
    min = scores[0][1]
    for i in range(0, N):
      if scores[i][1] <= min:
        min = scores[i][1]
        count += 1
    print(count)