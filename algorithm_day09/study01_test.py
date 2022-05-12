"""
<문제> : 최대공약수, 최소공배수
    두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 계산하여 출력
"""

# test


# 최대공약수1

n1 = 30
n2 = 24
min_01 = 0

if n1 < n2:
    min_01 = n1
else:
    min_01 = n2

for i in range(min_01, 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)
        break


# 최대공약수2

n1 = 30
n2 = 24

for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)
        break

# =======================================

# 최소공약수1

n1 = 30
n2 = 24
max_01 = 0

if n1 < n2 :
    max_01 = n2
else :
    max_01 = n1

for i in range(max_01, n1 * n1 +1):
    if i % n1 == 0 and i % n2 == 0:
        print(i)
        break

# 최소공약수2

n1 = 30
n2 = 24

for i in range(max(n1, n2), (n1 * n2) + 1):
    if i % n1 == 0 and i % n2 == 0:
        print(i)
        break
