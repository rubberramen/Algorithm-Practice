"""
<문제> : 소수 판별
    1보다 큰 임의의 정수를 입력받아 소수를 판별하라
"""

# 정답 출력 5로

n = 5
answer = "소수"

for i in range(2, n):
    # 2부터 n-1까지 나누어지는지 확인
    if n % i == 0:
        answer = "소수 아님"
        break    # 소수가 아님이 판단되면 break로 빠져나옴

print(f'{n} : {answer}')