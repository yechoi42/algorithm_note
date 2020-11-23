### 요구사항에 따라 적절한 알고리즘 설계하기

시간제한이 1초인 문제일 때

- N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘 설계
- N의 범위가 2000인 경우: 시간 복잡도가 O(N^2)인 알고리즘 설계
- N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘 설계
- N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘 설계



### 수행시간 측정 코드

```python
import time
start_time = time.time()

end_time = time.time()
print("time: ", end_time - start_time)
```

