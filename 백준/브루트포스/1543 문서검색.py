doc = list(input())
voca = list(input())
N = len(doc)
M = len(voca)

res = i = 0

for j in range(N):
    if i > j:
        continue
    if voca == doc[j:j+M]:
        res += 1
        i = j+M

print(res)