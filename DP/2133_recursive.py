import sys
sys.setrecursionlimit(100000)

N = int(input())
dp =[0] * (N + 1)

dp[0] = 1
if N >= 2:
    dp[2] = 3
def getDP(i):
    if i % 2:
        return 0
    if dp[i]:
        return dp[i]
    # dp[i - 2](2칸 줄인 경우)에 나머지 2칸을 만드는 경우의 수(3)을 곱함
    dp[i] += getDP(i - 2) * 3
    # 가로 길이 i - j의 경우에 j의 고유한 무늬 갯수 (2) 곱함 
    j = 4
    while (j <= i):
        dp[i] += getDP(i - j) * 2
        j += 2
    return dp[i]
answer = getDP(N)
print(answer)