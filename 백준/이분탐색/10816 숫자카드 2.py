# import sys
# n = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# chks = list(map(int, sys.stdin.readline().split()))


a, n = int(input()), sorted(list(map(int, input().split())))
b, m = int(input()), list(map(int, input().split()))

#n에 대한 딕셔너리 생성
n_dic = {}
for i in n :
    if i in n_dic :
        n_dic[i] += 1
    else :
        n_dic[i] = 1

# m에 있는 숫자가 n_dic에 있는지 확인
for k in m :
    print(n_dic.get(k, 0), end = ' ')
    
    # if k in n_dic :
    #     print(n_dic[k], end = ' ')
    # else :
    #     print(0, end = ' ')
