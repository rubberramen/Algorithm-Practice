"""
<문제>
    -(1/2)+(2/3)-(3/4)+(4/5)-(5/6)+(6/7) ... -(99/100)의 합계
    * 메서드를 만들어서 정답 출력
"""

def algorithm_day03():
    answer = 0
    for i in range(1, 100):
        a = i / (i + 1)
        if i % 2 != 0:
            answer -= a
        else:
            answer += a
    answer = round(answer, 6)
    return answer

print(f'정답 : {algorithm_day03()}')