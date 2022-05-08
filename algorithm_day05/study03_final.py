"""
<문제>
    1!+2!+3!+4!+5!+...+10!
    답 : 4037913
"""

# 정답 입력 받아서 : 1!+2!+3!+4!+5!+...+10! = 4037913

def day05_extend():
    n = int(input("숫자 n을 입력 : "))
    answer = 0
    for i in range(1, n+1):   # n으로 수정
        # 각 요소의 펙토리얼
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        # 펙토리얼 값 누적
        answer += factorial
    return answer

print(f'1!+2!+3!+4!+5!+...+n!의 정답 : {day05_extend()}')