a = list(map(int, input().split()))
anw = []
anw.append(1-a[0])
anw.append(1-a[1])
anw.append(2-a[2])
anw.append(2-a[3])
anw.append(2-a[4])
anw.append(8-a[5])

print(*anw)

print(' '.join(map(str,anw)))