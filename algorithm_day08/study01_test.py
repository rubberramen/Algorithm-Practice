"""
<문제> : 소수의 합
    임의의 정수를 입력 받아, 그 안에 포함된 소수의 합을 구하라
"""

# 테스트 및 밑그림

# 10 입력 받았다고 가정할때 : 2~10 사이에 속한 소수의 합 계산
# 2+3+5+7 = 17

n = 10
sum = 0

for i in range(2, 10+1):      # 2~10까지 소수인지 판단하고자
    isPrime = True            # 소수 여부 불린 변수
    for j in range(2, i):     # 특정 숫자가 소수인지 판단
        if i % j == 0:
            isPrime = False   # 나눠서 떨어지는 값 있으면, 소수 아님
            # break
            print(i)
        if isPrime == True:
            sum += i

print()
print(sum)

"""
>>> 이상하게 나옴 -> 두번째 if가 한단 앞으로 나와야 함
4
6
6
8
8
9
10
10

62

"""

