N, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()
count = 1
maximum = leaks[0] - 0.5 + L
for i in range(1, len(leaks)):
    if maximum < leaks[i] + 0.5:
        count += 1
        maximum = leaks[i] - 0.5 + L
print(count)