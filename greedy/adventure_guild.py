# 한 마을에 모험가 N명, 길드에서 이들을 대상으로 공포도 측정
# 공포도가 높으면 위험 상황에서 대처할 능력 떨어짐
# 길드장은 공포도가 X인 모험장은 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야
# 최대 몇 개의 모험가 그룹을 만들 수 있는가

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)