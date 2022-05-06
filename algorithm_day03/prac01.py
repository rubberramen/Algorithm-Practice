"""
<문제>
    -(1/2)+(2/3)-(3/4)+(4/5)-(5/6)+(6/7) ... -(99/100)의 합계
"""

answer = 0

for i in range(1, 100):
    a = i / (i + 1)
    if i % 2 != 0:
        answer -= a
    else:
        answer += a

print(f'정답 : {answer: .6f}')