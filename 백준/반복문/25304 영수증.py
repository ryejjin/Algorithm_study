x = int(input())
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
_sum = 0
for i in ls :
    _sum += i[0] * i[1]

if _sum == x :
    print('Yes')
else : print('No')
