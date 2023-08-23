from fractions import Fraction

n = int(input())
arr = list(map(int, input().split()))

for j in range(1, n):
    print(f'{Fraction(arr[0], arr[j]).numerator}/{Fraction(arr[0], arr[j]).denominator}')
