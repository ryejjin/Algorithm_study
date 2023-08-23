# 도화지 크기 100 * 100
# 색종이 크기 10 * 10 으로 고정
# n은 색종이 갯수, x.y 색종이 왼쪽 하단 좌표
n = int(input())
arr = [[0] * 101 for _ in range(101)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for _ in range(n):
    x, y = map(int, input().split())
    for s in range(y, y+10):
        for e in range(x, x+10):
            arr[s][e] = 1
length = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt  = 0
            for w in range(4):
                ni = i + di[w]
                nj = j + dj[w]
                if arr[ni][nj] == 1:
                    cnt += 1
            if cnt == 3:
                length += 1
            elif cnt == 2:
                length += 2
print(length)

# 둘레를 구하기 위해서 표시한 『1』의 상하좌우를 확인

# 상하좌우가 채워져 있으면 둘레에 해당되지 않습니다. → +0
# 한쪽 비어져 있으면 둘레에 해당됩니다. → +1
# 두 방향이 비어져 있으면 둘레에 해당됩니다. → +2 (모서리)
