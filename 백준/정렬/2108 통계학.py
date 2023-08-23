import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
_sum = sum(nums)
_len = len(nums)

nums_dict = {}
for num in nums:
    if num not in nums_dict.keys():
        nums_dict[num] = 1
    else :
        nums_dict[num] += 1

print(int(round(_sum/_len,0)))

print(nums[_len//2])

num_ls = list(nums_dict.items())
num_ls.sort(key = lambda x : (-x[1], x[0]))
if len(num_ls) == 1 :
    print(num_ls[0][0])
else :
    if num_ls[0][1] == num_ls[1][1] :
        print(num_ls[1][0])
    else : 
        print(num_ls[0][0])

print(nums[-1]-nums[0])


