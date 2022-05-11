"""
<문제> : 소수의 합
    임의의 정수를 입력 받아, 그 안에 포함된 소수의 합을 구하라
"""

# 10 입력 받았다고 가정할때, 정답 출력
# 2+3+5+7 = 17

n = 10
sum = 0                       # 합계(정답) 변수

for i in range(2, n+1):       # 2~n까지 소수인지 판단하고자
    isPrime = True            # 소수 여부 불린 변수
    for j in range(2, i):     # 특정 숫자가 소수인지 판단
        if i % j == 0:
            isPrime = False   # 나눠서 떨어지는 값 있으면, 소수 아님
            break
    if isPrime == True:       # 소수라면,
        sum += i              # 합계 sum 변수에 누적

print('answer :', sum)

"""
>>>

answer : 17
"""
