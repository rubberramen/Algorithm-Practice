"""
<문제> : 피보나치 수열
    1+1+2+3+5+8+13+... 의 수열로 나열되는 피보나치 수열의 20번째 항까지의 합계
    답 : 17710
"""

# 메서드 확장 : n값 입력받아, 메서드 파라미터로

n_input = int(input('n 입력 : '))

def day06_extend(n_input):
    a1 = 1
    a2 = 1
    n  = 2

    answer = a1 + a2

    while(n < n_input):
        temp = a1 + a2
        answer += temp
        a1 = a2
        a2 = temp
        n += 1

    return answer

print(f'피보나치 수열의 {n_input}번째 항까지의 합 : {day06_extend(n_input)}')