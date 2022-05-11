"""
<문제> : 소수 판별
    1보다 큰 임의의 정수를 입력받아 소수를 판별하라
"""

# 밑그림 : 10, 11

# 10

answer = "소수"

for i in range(2, 10):
    # 2부터 10-1까지 나누어지는지 확인
    if 10 % i == 0:
        answer = "소수 아님"
print(answer)

# 11
answer = "소수"

for i in range(2, 11):
    if 11 % i == 0:
        answer = "소수 아님"
print(answer)