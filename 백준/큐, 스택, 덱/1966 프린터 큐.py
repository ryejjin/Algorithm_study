from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    search = list(range(n+1))
    order = 0

    while arr:
        _max = max(arr)
        t = arr.popleft()
        m -= 1

        if _max == t:
            order += 1
            if m < 0:
                print(order)
                break

        else:
            arr.append(t)
            if m <0:
                m = len(arr)-1
