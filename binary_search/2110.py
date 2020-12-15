import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()
start = 1
end = max(homes) - min(homes)

def counter(mid):
    count = 1
    standard = homes[0] + mid
    for i in range(1, len(homes)):
        if homes[i] >= standard :
            count += 1
            standard = homes[i] + mid
    return (count)

result = 0
while start <= end:
    mid = (start + end) // 2
    if counter(mid) >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)