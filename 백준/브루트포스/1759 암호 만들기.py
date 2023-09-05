def comb(n, r):
    if r == 0:
        # 최소 한개의 모음과 최소 두개의 자음이 있어야하므로 각각의 갯수를 체크
        v = 0   # 모음
        c = 0   # 자음
        ans = ''
        for i in order:
            if i in (['a', 'e', 'o', 'u', 'i']):
                v += 1
            else:
                c += 1
            ans += i

        if v>0 and c>1:
            chk.append(ans)
    elif n < r:
        return
    else:
        order[r-1] = lst[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

l, c = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()

chk = []
order = [0]*l
comb(c, l)

chk.sort()
for j in chk:
    print(j)