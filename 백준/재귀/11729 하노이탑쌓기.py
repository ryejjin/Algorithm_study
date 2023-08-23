n = int(input())

def hanoi(n, s, m, e):
    if n == 0:
        return
    hanoi(n-1, s, e, m)
    print(s, e)
    hanoi(n-1, m, s, e)

print(2**n-1)
hanoi(n, 1, 2, 3)
