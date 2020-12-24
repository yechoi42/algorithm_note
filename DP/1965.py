n = int(input())
box = list(map(int, input().split()))
dp = [0] * n

dp[0] = 1
for i in range(1, n):
    arr = []
    for j in range(0, i):
        if box[j] < box[i]:
            arr.append(dp[j])
    if len(arr):
        dp[i] = max(arr) + 1
    else:
        dp[i] = 1
print(max(dp))