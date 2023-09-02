n = int(input())

def fibo(k) :
    if k == 0 :
        return 0
    elif k == 1 or k == 2 :
        return 1
    else :
        return fibo(k-1) + fibo(k-2)

a = fibo(n)
print(a)

def dp_fibo(k):
    