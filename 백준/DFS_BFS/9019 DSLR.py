from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b, result):
    q = deque([[a, result]])
    visit[a] = 1
    while q:
        t, res = q.popleft()
        if t == b:
            return res
        cal = [(t*2)%10000, t-1, (t%1000)*10+t//1000, ((t%10)*1000)+(t-(t%10))//10]
        for x in range(4):
            if x==0:
                temp = cal[x]
                if 0<=temp<10001 and visit[temp]==0:
                    q.append([temp, res+'D'])
                    visit[temp]=1
            if x==1:
                temp = cal[x]
                if temp == -1:
                    temp = 9999
                if 0<=temp<10001 and visit[temp]==0:
                    q.append([temp, res+'S'])
                    visit[temp] = 1
            if x==2:
                temp = cal[x]
                if 0<=temp<10001 and visit[temp]==0:
                    q.append([temp, res+'L'])
                    visit[temp] = 1
            if x==3:
                temp = cal[x]
                if 0<=temp<10001 and visit[temp]==0:
                    q.append([temp, res+'R'])
                    visit[temp] = 1


n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    visit = [0]*10001
    result = ''
    print(bfs(a, b, result))