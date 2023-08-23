import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
chks = list(map(int, sys.stdin.readline().split()))

start = 0
end = n - 1

def search(nums, target, start, end):
    mid = (start + end) // 2

    if start > end :
        return 0

    elif nums[mid] > target :
        return search(nums, target, start, mid - 1)
    
    elif nums[mid] < target :
        return search(nums, target, mid + 1, end)

    else :
        return 1

for target in chks :
    print(search(nums, target, start, end), end = ' ')

# a, n = input(), set(map(int, input().split()))
# b, m = input(), list(map(int, input().split()))
# for i in m :
#     if i in n : print(1, end = ' ')
#     else : print(0, end = ' ')
