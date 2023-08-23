n = int(input())
alpha = {}
for _ in range(n):
    voca = input()
    for i in range(len(voca)):
        if voca[i] not in alpha.keys():
            alpha[voca[i]] = 0

    for i in range(len(voca)):
        alpha[voca[i]] += 10**(len(voca)-i-1)

chk = sorted(list(alpha.values()))
num = 9
anw = 0
for j in range(len(chk)-1,-1,-1):
    anw += chk[j] * num
    num -= 1

print(anw)