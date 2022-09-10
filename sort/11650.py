from functools import cmp_to_key
import sys

# def comparator(a,b):
#     if a[0] == b[0]:
#         if a[1] > b[1]:
#             return 1
#         else:
#             return -1
#     else:
#         return a[0] - b[0]

T = int(sys.stdin.readline())
points =[]
for _ in range(T):
    X, Y = map(int, input().split())
    points.append((X,Y))
points = sorted(points)
for i in range(T):
    print(points[i][0], points[i][1])
