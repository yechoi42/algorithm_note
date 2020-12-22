N = int(input())
T = []
P = []
dp = []

for i in range(N):
    a, b = map(int, input().split(" "))
    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0)

for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])
    else:
        dp[i] = dp[i + 1]
print(max(dp))