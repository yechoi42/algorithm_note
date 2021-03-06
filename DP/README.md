# 다이나믹 프로그래밍
이미 계산된 결과는 별도의 메모리 영역에 저장해 다시 계산하지 않도록
구현은 두가지, 탑다운과 보텀업으로 구성

## 다이나믹 프로그래밍의 조건
1. 최적 부분구조<br>
큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
2. 중복되는 부분 문제<br>
동일한 작은 문제를 반복적으로 해결

## 다이나믹 프로그래밍 유형 파악하기
그리디, 구현, 완전 탐색 등으로 해결할 수 있는지 검토
다른 알고리즘 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려
재귀함수로 비효울적인 완전 탐색 프로그램을 작성, 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면 코드를 개선
**일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 주로 출제됨**

## 보텀업
전형적인 형태
결과 저장용 리스트는 DP 테이블이라고 부름 

```
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
return (d[n])
```

## 메모이제이션
한번 계산한 결과를 메모리 공간에 메모하는 기법
같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
값을 기록해 놓는다는 점에서 캐싱(cashing)이라고도 함
시간복잡도는 O(N)

```
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
```

# 분할정복(퀵정렬)
한번 기준 원소(pivot)가 자리를 잡으면 그 기준 원소의 위치는 바귀지 않음
분할 이후 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않음 

