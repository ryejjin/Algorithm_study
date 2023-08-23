t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))[1:]
    line = [arr[0]]
    cnt = 0
    for i in range(1, 20):
        for j in range(len(line)):
            if arr[i] < line[j]:
                cnt += (len(line) - j)
                line.insert(j, arr[i])
                break
        else:
            line.append(arr[i])
    print(f'{tc} {cnt}')