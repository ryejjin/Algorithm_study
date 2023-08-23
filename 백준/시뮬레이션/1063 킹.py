# i, j 위치에 유념/ 체스판 아래쪽부터 1~8임
alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
num = {1: 'A', 2:'B', 3:'C', 4:'D', 5 :'E', 6:'F', 7:'G', 8:'H'}
king, stone, n = map(str, input().split())
# 초기 king과 stone의 위치
ki, kj = int(king[1]), int(alpha[king[0]])
si, sj = int(stone[1]), int(alpha[stone[0]])
# 조건
# 1) king을 옮긴 위치와 돌의 위치가 같으면 > 돌도 똑같이 옮김 > 옮긴 돌이 유효한 범위에 있는지 확인 > 유효범위가 아니면 모두 제자리
# 2) 옮긴 king의 위치가 돌과 다르면 > 옮긴 king이 유효한 범위인지 확인 > 유효하지 않으면 원위치
for _ in range(int(n)):
    m = input()
    if m == 'R':
        nki, nkj = ki, kj+1
        if si == nki and sj == nkj:
            nsi, nsj = si, sj + 1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'L':
        nki, nkj = ki, kj-1
        if si == nki and sj == nkj:
            nsi, nsj = si, sj - 1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'B':
        nki, nkj = ki-1, kj
        if si == nki and sj == nkj:
            nsi, nsj = si-1, sj
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'T':
        nki, nkj = ki+1, kj
        if si == nki and sj == nkj:
            nsi, nsj = si+1, sj
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'RT':
        nki, nkj = ki+1, kj+1
        if si == nki and sj == nkj:
            nsi, nsj = si+1, sj + 1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'LT':
        nki, nkj = ki+1, kj-1
        if si == nki and sj == nkj:
            nsi, nsj = si+1, sj-1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'RB':
        nki, nkj = ki-1, kj+1
        if si == nki and sj == nkj:
            nsi, nsj = si-1, sj + 1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
    elif m == 'LB':
        nki, nkj = ki-1, kj-1
        if si == nki and sj == nkj:
            nsi, nsj = si-1, sj-1
            if 1<=nsi<9 and 1<=nsj<9:
                si, sj = nsi, nsj
                ki, kj = nki, nkj
        else:
            if 1<=nki<9 and 1<=nkj<9:
                ki, kj = nki, nkj
# i, j 위치 반대로해서 출력도 반대로
print(num[kj], ki, sep='')
print(num[sj], si, sep='')