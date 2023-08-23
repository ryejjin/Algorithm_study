ls = []
for _ in range(5):
    ls.append(int(input()))
_sum = sum(ls)
_len = len(ls)
print(int(_sum/_len))
ls.sort()
print(ls[len(ls)//2])
