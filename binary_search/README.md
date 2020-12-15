# 이진탐색
단계마다 탐색 범위를 2로 나누는 것과 동일하므로 시간복잡도는 O(logN)을 보장
탐색 범위가 클 때 가장 먼저 이진탐색을 떠올려야

## 재귀적 구현
```
def binary_search(array, target, start, end):
    if start > end:
        retur None
    mid = (start + end) // 2
    if (array[mid] == target):
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
```


## 반복문 구현
```
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return (None)
```


## 특정 범위에 속하는 데이터 개수 구하기
```
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
```

## 파라메트릭 서치
최적화문제를 결정문제(예 || 아니오)로 바꿔 해결하는 기법
이진탐색을 활용해 풂
예) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제