import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    path = []
    Q = deque()
    flag = 1
    for i in range(1, N+1):
        if D[i] == 0:
            if flag == 0:
                return '?'
            else:
                Q.append(i)
                flag = 0

    if not Q:
        return 'IMPOSSIBLE'

    while Q:
        v = Q.popleft()
        path.append(grade[v])

        flag = 1
        for w in range(1, N+1):
            if D[w] > 0:
                D[w] -= 1
                if D[w] == 0:
                    if flag:
                        Q.append(w)
                        flag = 0
                    else:
                        return '?'
    if len(path) != N:
        return 'IMPOSSIBLE'
    return path


T = int(input())
for _ in range(T):
    N = int(input())
    grade = [0] + list(map(int, input().split()))
    M = int(input())
    D = [0] + [i for i in range(N)]
    for _ in range(M):
        s, e = map(int, input().split())
        # 상대적인 등수가 바뀌는 것
        if grade.index(s) > grade.index(e):
            D[grade.index(s)] -= 1
            D[grade.index(e)] += 1
        else:
            D[grade.index(s)] += 1
            D[grade.index(e)] -= 1
    print(D)

    path = bfs()
    if type(path) == str:
        print(path)
    else:
        print(*path)