def fibona(n):          #재귀호출 의사 코드
    if n == 1 or n == 2:
        return 1
    else:
        return fibona(n-1) + fibona(n-2)


def fibo(n):            #동적프로그래밍 의사 코드
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    cnt = 0
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1
    return cnt

n = int(input())
print(fibona(n), fibo(n))


#재귀함수의 호출 횟수는 실행횟수와 동일하다
#dp는 실행될때마다 cnt += 1해줌
