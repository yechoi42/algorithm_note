n, m = map(int, input().split())

cards = list(map(int, input().split()))
answer = 0
for i in range(n - 2):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            hap = cards[i] + cards[j] + cards[k]
            if m - hap >= 0 and answer < hap:
                answer = hap
print(answer)