s = input()
ls = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        ls.append(s[i:j])
anw = len(set(ls))
print(anw)