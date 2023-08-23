voca = list(input())
boom = list(input())
stack = []
for i in voca:
    stack.append(i)
    if i == boom[-1]:
        if len(stack) >= len(boom):     # stack이 폭발할 문자열보다 크거나 같아야 폭발가능하기 때문
            n = len(boom)
            if stack[-n:] == boom:
                for j in range(n):
                    stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(*stack, sep='')