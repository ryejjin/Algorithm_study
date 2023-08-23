n, m = map(int, input().split())
r = 1                       # 서로소의 최대공약수는 1이다.
lc = n * m                  # 최대공배수 구하기 위해서 미리 곱해둠
if n < m :                  # 둘 중 더 큰 수 찾기 위함
    n, m = m, n

if n % m == 0 :             # 큰 수에서 작은수를 나눴을 때 나머지가 0이면 더 작은 수가 최대공약수
    r = m                   

# 유클리드 호제법

# A와 B를 나눈 몫이 Q 나머지가 R일 때
# gcd(A,B) = gcd(B, R) 이다

else :
    while n % m != 0:
        r = n % m
        n = m
        m = r

print(r)
print(int(lc / r))