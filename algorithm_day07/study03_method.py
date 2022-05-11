"""
<문제> : 소수 판별
    1보다 큰 임의의 정수를 입력받아 소수를 판별하라
"""

# 메서드
def day07(n):
    answer = "소수"
    for i in range(2, n):
        if n % i == 0:
            answer = "소수 아님"
            break
    return f'{n} : {answer}'

print(day07(7))
print(day07(11))
print(day07(20))