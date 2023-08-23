# 중복 순열

def perm(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next
x = input()
lst = list(x)
n = len(lst)
chk = []
for i in perm(lst, n):
    a = ''
    for j in i:
        a += j
    chk.append(a)

anw = []
for k in chk:
    anw.append(int(k))
anw = list(set(anw))
anw.sort()
if int(x) == anw[-1]:
    print(0)
else:
    print(anw[anw.index(int(x))+1])