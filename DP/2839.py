n = int(input())
dp = [-1] * (n + 1)
if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1
for i in range(6, n + 1):
    if dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:
        if dp[i] != -1:
            dp[i] = min(dp[i], dp[i - 5] + 1)
        else:
            dp[i] = dp[i - 5] + 12
print(dp[n]) 
