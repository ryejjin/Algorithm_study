n = int(input())
arr = list(map(int, input().split()))
line = []
student = 1
for i in range(n):
    line.insert(arr[i],student)
    student += 1
line = line[::-1]
print(*line, end = ' ')

# for i in range(n):
#     if len(line[arr[i]]) != 0:
#         t = line[arr[i]].pop()
#         line[arr[i]+1].append(t)
#         line[arr[i]].insert(0,student)
#     else:
#         line[arr[i]].append(student)
#     student += 1
# line = list(filter(None, line))
# line = line[::-1]
# for k in line:
#     print(*k, end = ' ')