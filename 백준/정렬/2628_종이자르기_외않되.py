x, y = map(int, input().split())
n = int(input())
idx_x = [i for i in range(1, y+1)]   #가로
idx_y = [j for j in range(1, x+1)]   #세로
for _ in range(n):
    s, e = map(int, input().split())
    if s == 0:  #가로
        idx_x.insert(e, 0)
    elif s == 1:    #세로
        idx_y.insert(e, 0)
idx_x.append(0)
idx_y.append(0)
cnt = 0
width = []
length = []
for k in idx_x:
    if k != 0:
        cnt += 1
    if k == 0:
        width.append(cnt)
        cnt = 0
cnt2 = 0
for l in idx_y:
    if l != 0:
        cnt2 += 1
    if l == 0:
        length.append(cnt2)
        cnt2 = 0
anw = []
for a in width:
    for b in length:
        anw.append(a*b)

print(max(anw))