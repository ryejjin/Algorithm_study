def powerset(n, k):
    global anw
    if n == k:
        chk = []
        for i in range(n):
            if bit[i] == 1:
                chk.append(nanjang[i])
                if len(chk) == 7 and sum(chk) == 100:
                    chk = sorted(chk)
                    anw.append(chk)
        return anw
    else:
        bit[k] = 1
        powerset(n, k+1)
        bit[k] = 0
        powerset(n, k+1)

nanjang = []
for _ in range(9):
    nanjang.append(int(input()))
N = len(nanjang)
bit = [0] * N
anw = []
powerset(N, 0)
for j in range(7):
    print(anw[0][j])