'''
1) 두 선이 겹치고, 그 때 꺼낸 도착점이 end보다 뒤에 있는 경우
> start는 그대로 두고, end는 꺼낸 도착점으로 업데이트
2) 두 선이 겹치고, 꺼낸 도착점이 end보다 앞에 있는 경우
> start, end 둘 다 그대로 둔다
3) 두 선이 겹치지 않는 경우
> 그 길이를 ans에 더한 후, 시작점과 도착점을 start와 end로 업데이트
'''

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])

s = arr[0][0]
e = arr[0][1]

res = 0

for i in range(1, n):
    ns, ne = arr[i]

    if e>ns:
        e = max(e, ne)
    else:
        res += e-s
        s, e = ns, ne
res += (e-s)
print(res)