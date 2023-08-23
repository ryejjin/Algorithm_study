# 2트
# 최초의 k번째까지의 합을 구한 후 첫번째값은 빼주고, k번째의 숫자를 더해줌으로써 불필요한 연산을 줄임
n, k = map(int, input().split())
arr = list(map(int, input().split()))
chk = sum(arr[:k])
sum_arr = [chk]

for i in range(n-k):
    chk = chk - arr[i] + arr[i+k]
    sum_arr.append(chk)

print(max(sum_arr))


# 처음 풀이(범위가 커서 시간 초과/ 정답은 나옴!)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
_max = 0
for i in range(n-k):
    chk = 0
    for j in range(k):
        chk += arr[i+j]
    if chk > _max:
        _max = chk

print(_max)