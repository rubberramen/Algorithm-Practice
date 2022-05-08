"""
<문제>
    1!+2!+3!+4!+5!+...+10!
    답 : 4037913
"""

# 1!+2!+3!+4! = 1+2+6+24=33

answer = 0
for i in range(1, 4+1):
    # 각 요소의 펙토리얼
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    print(factorial)
    # 펙토리얼 값 누적
    answer += factorial

print()
print(answer)

# 1!+2!+3!+4!+5! = 1+2+6+24+120 = 153
print('==============================')

answer = 0
for i in range(1, 5+1):

    # 각 요소의 펙토리얼
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    # print(factorial)
    answer += factorial

print(answer)


# 1!+2!+3!+4!+5!+...+10! = 4037913
print('==============================')

answer = 0
for i in range(1, 10+1):

    # 각 요소의 펙토리얼
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    # print(mul)
    answer += factorial

print(answer)

# 1!+2!+3!+4!+5!+...+10! = 4037913
print('==============================')

answer = 0
for i in range(1, 10+1):
    # 각 요소의 펙토리얼
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    # 펙토리얼 값 누적
    answer += factorial

print(f'정답 : {answer}')