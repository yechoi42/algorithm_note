n = int(input())
sinkers = list(map(int, input().split()))
sinkers.sort()

sum = 0
for i in range(n):
    if sum + 1 < sinkers[i]:
        break
    sum += sinkers[i]

print(sum + 1) 