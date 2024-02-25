# 두 가지 방식으로 풀이가 가능 (모든 경우를 봐야하기 때문에 브루트포스로 분류 가능)
# 1. 순열방식 : 연산자를 고정하고 숫자를 이동하는 방법 (N!개)
# 2. DFS + 백트래킹 : 숫자를 고정하고 연산자를 이동 (2*(n-1)개) > 메모리, 시간적으로 더 유리


n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

# 초기화를 정수형으로 해줘야함
max_v = int(-1e9)
min_v = int(1e9)

#함수 구현
def dfs(cnt, result, add, sub, mul, div) :
    global max_v, min_v

    if cnt == n :                   #cnt가 n이 되었을 때 max와 min을 반환 (함수종료)
        max_v = max(result, max_v)
        min_v = min(result, min_v)
        return
    if add > 0 :
        dfs(cnt+1, result + num[cnt], add-1, sub, mul, div)
    if sub > 0 :
        dfs(cnt+1, result - num[cnt], add, sub-1, mul, div)
    if mul > 0 :
        dfs(cnt+1, result * num[cnt], add, sub, mul-1, div)
    if div > 0 :
        dfs(cnt+1, int(result/num[cnt]), add, sub, mul, div-1)

dfs(1, num[0], add, sub, mul, div)
print(max_v)
print(min_v)