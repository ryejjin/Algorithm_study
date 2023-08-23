n = int(input())
sl = [list(map(int, input().split())) for _ in range(n)]
island = [False] * n

def team(l, k):
    star, link = 0, 0
    if k == n/2 :
        for i in range(n):
            for j in range(i+1,n):
                if island[i] and island[j] :
                    star += sl[i][j] + sl[j][i]
                if not island[i] and not island[j]:
                    link += sl[i][j] + sl[j][i]
        return abs(star - link)
    res = 10 ** 9
    for w in range(l,n):
        island[w] = True
        _min = team(w+1, k+1)
        if _min < res :
            res = _min
        island[w] = False
    return res

print(team(0,0))