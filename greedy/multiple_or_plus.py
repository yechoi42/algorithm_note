# 각 자리가 숫자로 이뤄진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자사이에 X 또는 +연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰수를 구하는 프로그램을 작성하세요.
# 단 +보다 x를 먼저 계산하는 일반적인 방식과 달리 모든 연산은 왼쪽부터 순서대로 이뤄진다.

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)