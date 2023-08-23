squ = [list(map(int, input().split())) for _ in range(9)]

_max = -1
_i = 0
_j = 0

for i in range(9):
    for j in range(9):
        if squ[i][j] >= _max :
            _max = squ[i][j]
            _i = i + 1
            _j = j + 1

print(_max)
print(_i, _j)