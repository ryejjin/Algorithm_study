while True:
    s = input()
    is_balan = True
    if s == '.':
        break
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')' or i == ']':
            if len(stack) != 0:
                a = stack.pop()
                if i == ')' and a != '(':
                    is_balan = False
                    break
                elif i == ']' and a != '[':
                    is_balan = False
                    break
            else:
                is_balan = False
                break
    if is_balan == True and len(stack) == 0:
        print('yes')
    else:
        print('no')