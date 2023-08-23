import sys
input = sys.stdin.readline

def comb(n, r, k, s):
    if k == r:
        print(*rotto)
    else:
        for i in range(s, n-r+1+k):
            rotto[k] = arr[i]
            comb(n, r, k+1, i+1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        n = arr[0]
        arr = arr[1:]
        rotto = [0]*6
        comb(n, 6, 0, 0)
        print()