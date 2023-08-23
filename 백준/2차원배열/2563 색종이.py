paper = [[0]*100 for _ in range(100)] #100*100 도화지 생성
t = int(input()) #입력
for _ in range(t):
    m, n = map(int, input().split())
    for i in range(m, m+10):
        for j in range(n, n+10):
            paper[i][j] = 1 #겹쳐도 이미 1이기때문에 유지됨

cnt = 0
for i in range(100):
    for j in range(100):
        cnt += paper[i][j] #paper안에 1과 0밖에 없기 때문에 이 형태가 가능

print(cnt)

