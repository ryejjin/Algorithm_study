# n = list(input() for _ in range(int(input())))
# n_1 = list(map(int, n))
# n_1.sort()

# for i in range(len(n_1)):
#     print(n_1[i])

import sys
num = [0]*10001
for _ in range(int(sys.stdin.readline().strip())): #수의 갯수
    a = int(sys.stdin.readline().strip())        #갯수만큼 숫자 입력
    num[a] += 1         #리스트에 입력된 숫자의 인덱스에 1 더해줌(갯수 세아리기)

for i in range(len(num)) : 
    if num[i] == 0 :        #리스트에 없는 숫자들 제하기
        continue
    while num[i] > 0 :      #리스트에 저장되어 있는만큼 프린트
        print(i)
        num[i] -= 1
