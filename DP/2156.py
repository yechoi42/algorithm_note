import sys
sys.setrecursionlimit(100000)

n = int(input())
wine = []
dp = [-1] * n
for _ in range(n):
    wine.append(int(input()))

def getdp(i):
    if i == 0:
        dp[0] = wine[0]
        return dp[i]
    elif i == 1:
        dp[1] = wine[0] + wine[1]
        return dp[i]
    elif i < 0:
        return 0
    if dp[i] == -1:
        dp[i] = max(getdp(i - 3) + wine[i - 1] + wine[i], getdp(i - 2) + wine[i], getdp(i - 1))
    return (dp[i])

answer = getdp(n - 1)
print(answer)