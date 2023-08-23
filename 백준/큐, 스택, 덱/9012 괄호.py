t = int(input())
for _ in range(t):
    ls = input()

    _open = []
    for i in range(len(ls)):
        if ls[i] == '(':
            _open.append(i)
        if ls[i] == ')':
            if  len(_open) != 0 :
                _open.pop()
            else : 
                print('NO')
                break
    else :        
        if len(_open) != 0 :
            print('NO')
        else :
            print('YES')
                