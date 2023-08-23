import sys
input = sys.stdin.readline

n = int(input())

def checkPrime(x):
    for i in range(2, int(x**0.5)+1):
        if int(x)%i ==0:
            return False
    return True


def makenumber(k):
    if len(str(k))==n:
        print(k)
    else:
        for i in range(10):
            temp = k*10+i
            if checkPrime(temp) == True:
                makenumber(temp)

makenumber(2)
makenumber(3)
makenumber(5)
makenumber(7)