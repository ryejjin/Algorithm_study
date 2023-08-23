import sys
input = sys.stdin.readline

def binary_search(x):
    s, e = 0, len(lst)-1
    while s<=e:
        mid = (s+e)//2
        if x <= lst[mid]:
            e = mid-1
        elif x > lst[mid]:
            s = mid+1
    return s


n = int(input())
arr = list(map(int, input().split()))
lst = [0]
for i in arr:
    if lst[-1] < i :
        lst.append(i)
    else:
        lst[binary_search(i)] = i

print(len(lst)-1)