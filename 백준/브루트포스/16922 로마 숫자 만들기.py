def combi(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i:], r-1):
                yield [arr[i]] + next

n = int(input())
lst = [1, 5, 10, 50]
anw = []
for i in combi(lst, n):
    anw.append(sum(i))

anw = set(anw)
print(len(anw))