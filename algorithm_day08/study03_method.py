"""
<문제> : 소수의 합
    임의의 정수를 입력 받아, 그 안에 포함된 소수의 합을 구하라
"""

# 메서드

def day08(n):
    sum = 0                        # 합계(정답) 변수

    for i in range(2, n+1):        # 2~n까지 소수인지 판단하고자
        isPrime = True             # 소수 여부 불린 변수
        for j in range(2, i):      # 특정 숫자가 소수인지 판단
            if i % j == 0:
                isPrime = False    # 나눠서 떨어지는 값 있으면, 소수 아님
                break
        if isPrime == True:        # 소수라면,
            sum += i               # 합계 sum 변수에 누적
    return sum                     # 결과 리턴

# 정답 출력
n = int(input('n 입력 : '))
print(f'{n} 이하 소수의 합 : {day08(n)}')

"""
>>>

n 입력 : 10
10 이하 소수의 합 : 17
"""