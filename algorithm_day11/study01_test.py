"""
<문제> : 소인수 분해하기
    정수를 입력 받아, 소인수를 구해 출력하시오
"""

# 소수 판별 메서드      # day07 알고리즘 응용

def isPrime(n):
    answer = True
    for i in range(2, n):
        if n % i == 0:
            answer = False
            break
    return answer

# print(isPrime(11))

# ==========================================================

# n이하 소수 찾는 메서드

def findPrimes(n):
    primes = []                # n이하 소수를 담을 리스트 생성
    for i in range(2, n+1):
        if isPrime(i):         # 소수이면,
            primes.append(i)   # 리스트에 추가
    return primes

# print(findPrimes(12))

# ==========================================================

# n 소인수 분해 : n = 60

n = 60

factors = []
primes = findPrimes(n)  # n의 소수 리스트를 추출
for i in primes:
    while n % i == 0 :  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
        factors.append(i)
        n = n // i

print(factors)