ls = []
for _ in range(28):
    ls.append(int(input()))

cnt = 0
anw = []
for k in range(1, 31):
    if k not in ls:
        anw.append(k)
anw.sort()
for j in anw :
    print(j)