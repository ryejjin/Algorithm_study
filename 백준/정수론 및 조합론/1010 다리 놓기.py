import itertools

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    def nume(m):
        if m == 0 :
            return 1
        return m * nume(m-1)
    
    def demo(n, m):
        if m - n == 0:
            return 1
        return (m - n) * demo(n, m-1)

    anw = nume(m) // (nume(n) * demo(n, m))
    print(anw)