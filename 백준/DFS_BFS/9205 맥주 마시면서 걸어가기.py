t = int(input())
for tc in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    store.sort(key=lambda x: (x[0], x[1]))
    fx, fy = map(int, input().split())

    ans = 'happy'
    for i in range(n):
        beer = 20
        dis = abs(store[i][0]-hx) + abs(store[i][1]-hy)
        if dis > 50 * beer:
            ans = 'sad'
            break
        else:
            hx, hy = store[i][0], store[i][1]
            beer -= dis//50

    if ans == 'happy':
        beer = 20
        if abs(fx-hx) + abs(fy-hy) >= beer * 50:
            ans = 'happy'
        else:
            ans = 'sad'

    print(ans)