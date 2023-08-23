import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

frame = []
order = 1

for s in arr:
    if len(frame) == 0:
        frame.append([s, 0, order])
        order += 1
    elif len(frame) < n:
        for i in range(len(frame)):
            if s == frame[i][0]:
                frame[i][1] += 1
                break
        else:
            frame.append([s, 0, order])
            order += 1

    elif len(frame) >= n:
        for i in range(len(frame)):
            if s == frame[i][0]:
                frame[i][1] += 1
                break
        else:
            frame.sort(key=lambda x:(x[1], x[2]))
            frame.remove(frame[0])
            frame.append([s, 0, order])
            order += 1

frame.sort(key=lambda x:x[0])

for x in range(len(frame)):
    print(frame[x][0], end = ' ')