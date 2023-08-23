import sys
input = sys.stdin.readline

arr = list(input())

one = zero = 0
for i in range(len(arr)-1):
    if arr[i] != arr[i+1] and arr[i] == '0':
        zero += 1
    elif arr[i] != arr[i+1] and arr[i] == '1':
        one += 1

print(min(zero, one))