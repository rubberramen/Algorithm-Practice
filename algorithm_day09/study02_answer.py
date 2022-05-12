"""
<문제> : 최대공약수, 최소공배수
    두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 계산하여 출력
"""

# 메서드

# 최대공약수

n1 = 30
n2 = 24

def GCD(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
            break

print(f'{n1}, {n2}의 최대공약수 : {GCD(n1, n2)}')

# 최소공배수

n1 = 30
n2 = 24

def LCM(n1, n2):
    if n1 < n2 :
        max = n2
    else :
        max = n1

    for i in range(max, n1 * n1 +1):
        if i % n1 == 0 and i % n2 == 0:
            return i
            break

print(f'{n1}, {n2}의 최소공배수 : {LCM(n1, n2)}')