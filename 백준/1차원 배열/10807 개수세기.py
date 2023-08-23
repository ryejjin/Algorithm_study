n = int(input())
num_ls = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in num_ls :
    if i == v :
        cnt += 1

print(cnt)