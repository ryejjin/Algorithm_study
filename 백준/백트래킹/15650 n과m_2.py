##조합
import itertools            

n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)         

result = ''.join(map(str, nums))   
anw = list(map(' '.join, itertools.combinations(result, m)))
for k in anw:
    print(k)