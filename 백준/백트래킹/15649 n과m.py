##순열
import itertools            #순열 함수를 쓰기 위한 선언

n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)          #n까지 들어 있는 list를 생성

result = ''.join(map(str, nums))    #순열 생성 함수를 사용하기 위해서는 str이 필요해서 map을 이용한 변환

anw = list(map(' '.join, itertools.permutations(result, m)))
for k in anw:
    print(k)