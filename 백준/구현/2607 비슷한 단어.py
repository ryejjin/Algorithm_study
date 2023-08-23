n = int(input())
first = list(input())
count = 0
for _ in range(n-1):
    compare = first[:]
    word = input()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) <2:
        count += 1

print(count)