import sys
n = int(sys.stdin.readline())

room_se = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

room_se.sort(key = lambda x : (x[1], x[0]))     #회의실 시간 리스트를 끝나는 시간 기준 > 시작하는 시간 기준 순으로 오름차순 정렬

cnt = 0
end = 0

for time in room_se:            #시간은 room_se에서
    if time[0] >= end :         #시작하는 시간이 끝나는 시간보다 크거나 같으면
        cnt += 1                #횟수에 1을 더해주고
        end = time[1]           #끝나는 시간을 end에 저장

print(cnt)