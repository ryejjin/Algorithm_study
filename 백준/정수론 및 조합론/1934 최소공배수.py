t = int(input())
r = 1

for tc in range(t):
    a, b = map(int, input().split())
    lc = a * b

    if a < b :
        a, b = b, a

    if a % b == 0 :
        r = b

    else :
        while a % b != 0:
            r = a % b
            a = b
            b = r

    print(int(lc/r))

