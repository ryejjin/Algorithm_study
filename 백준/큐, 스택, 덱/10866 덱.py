from collections import deque
import sys
nums  = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    qu = list(map(str, sys.stdin.readline().split()))

    if qu[0] == 'push_front' :
        nums.appendleft(qu[1])
    if qu[0] == 'push_back' :
        nums.append(qu[1])
    if qu[0] == 'pop_front' :
        if len(nums) == 0 : 
            print(-1)
        else:
            print(nums.popleft())
    if qu[0] == 'pop_back' :
        if len(nums) == 0 :
            print(-1)
        else:
            print(nums.pop())
    if qu[0] == 'size':
        print(len(nums))
    if qu[0] == 'empty':
        if len(nums) == 0: 
            print(1)
        else:
            print(0)
    if qu[0] == 'front':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
    if qu[0] == 'back':
        if len(nums) == 0: 
            print(-1)
        else:
            print(nums[-1])
