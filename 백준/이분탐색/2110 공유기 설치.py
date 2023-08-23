n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])

# 집 간의 거리를 이분탐색으로 줄여주기
start = 1
end = home[-1] - home[0]
result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 1
    cur = home[0]           # 현재 집 위치
    for i in range(1,n):
        if home[i] >= cur + mid:    # 현재 집 위치에서 거리를 더했을 때 집이 더 멀면 공유기 설치
            cnt += 1
            cur = home[i]

    if cnt >= c:            # 공유기가 더 많이 설치됐으면 거리를 늘려줘야 함
        start = mid + 1
        result = mid
    else:                   # 갯수가 적으면 거리를 줄여줌
        end = mid - 1

print(result)