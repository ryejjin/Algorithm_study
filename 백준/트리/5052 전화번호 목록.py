t = int(input())
for _ in range(t):
    n = int(input())
    phones = []
    for _ in range(n):
        phone = list(map(int, input()))
        phones.append(phone)
    phones.sort()

    for i in range(n-1):
        if phones[i] == phones[i+1][:len(phones[i])]:
            print('NO')
            break
    else:
        print('YES')