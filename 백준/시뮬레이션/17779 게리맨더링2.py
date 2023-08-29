import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

# dis5를 구하기 위함
total = 0
for i in arr:
    total += sum(i)

def district(x, y, d1, d2):
    global total, ans
    one = two = three = four = 0

    # dis 1
    col1 = y+1
    for r in range(x+d1):
        if r>=x:
            col1 -= 1
        one += sum(arr[r][:col1])

    # dis 2
    col2 = y+1
    for r in range(x+d2+1):
        if r > x:
            col2 += 1
        two += sum(arr[r][col2:])

    # dis 3
    col3 = y-d1
    for r in range(x+d1, n):
        three += sum(arr[r][:col3])
        if r < x+d1+d2:
            col3+=1

    # dis 4
    col4 = (y+d2) - n
    for r in range(x+d2+1, n):
        four += sum(arr[r][col4:])
        if r<=x+d1+d2:
            col4-=1

    # dis 5
    five = total - one - two - three - four
    ans = min(ans, (max(one, two, three, four, five)-min(one, two, three, four, five)))


def check(x, y, d1, d2):
    if 1<=x+d1-1<n and 0<=x+d2-1<n and 0<=y-d1+d2-1<n:
        if 0<=y-d1 and y+d2<n and x+d1+d2<n:
            district(x, y, d1, d2)


for x in range(n-2):
    for y in range(1, n-1):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                check(x, y, d1, d2)

print(ans)