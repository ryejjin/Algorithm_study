import sys
from collections import deque
input = sys.stdin.readline

## 매번 뒤집으면 시간초과 발생
## flag를 사용해서 마지막에 한번만 뒤집어 줌.

for tc in range(int(input())):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    flag = 0
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(arr) == 0:
                print("error")
                break
            else:
                if flag%2:
                    arr.pop()
                else:
                    arr.popleft()
    else:
        if flag%2:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")