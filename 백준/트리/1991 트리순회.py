dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
       'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,
       'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '.':0}
alpha = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K',
         12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U',
         22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

def preorder(v):
    if v!=0:
        print(alpha[v], end ='')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v!=0:
        inorder(tree[v][0])
        print(alpha[v], end='')
        inorder(tree[v][1])

def postorder(v):
    if v!=0:
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(alpha[v], end='')

n = int(input())
tree = [[0]*3 for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(str, input().split())
    p, l, r = dic[a], dic[b], dic[c]
    tree[p][0] = l
    tree[p][1] = r
    if l != 0:
        tree[l][2] = p
    if r != 0:
        tree[r][2] = p

preorder(1); print()
inorder(1); print()
postorder(1)
