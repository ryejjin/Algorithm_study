a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

# print(len(a_set ^ b_set))
c_set = set()
for i in a_set :
    if i in b_set :
      c_set.add(i)  

print(len(a_set) + len(b_set) - 2 * len(c_set))