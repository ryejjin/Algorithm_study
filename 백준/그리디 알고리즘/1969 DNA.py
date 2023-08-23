import sys
input = sys.stdin.readline

n, m = map(int, input().split())
DNA = [list(input()) for _ in range(n)]

cnt = 0
dna = ''
for i in range(m):
    count = [0, 0, 0, 0]
    for j in range(n):
        if DNA[j][i] == 'A':
            count[0] += 1
        elif DNA[j][i] == 'C':
            count[1] += 1
        elif DNA[j][i] == 'G':
            count[2] += 1
        elif DNA[j][i] == 'T':
            count[3] += 1
    idx = count.index(max(count))
    if idx == 0:
        dna += 'A'
    elif idx == 1:
        dna += 'C'
    elif idx == 2:
        dna += 'G'
    elif idx == 3:
        dna += 'T'
    cnt += n-max(count)

print(dna)
print(cnt)