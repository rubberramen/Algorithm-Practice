"""
<문제> : 피보나치 수열
    1+1+2+3+5+8+13+... 의 수열로 나열되는 피보나치 수열의 20번째 항까지의 합계
    답 : 17710
"""

# 메서드

def day06():
    a1 = 1
    a2 = 1
    n  = 2

    answer = a1 + a2

    while(n < 20):
        temp = a1 + a2
        answer += temp
        a1 = a2
        a2 = temp
        n += 1

    return answer

print(f'피보나치 수열의 20번째 항까지의 합 : {day06()}')