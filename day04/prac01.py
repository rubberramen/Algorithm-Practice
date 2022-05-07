"""
<문제>
    1+2+4+7+11+16+22+...의 순서로 나열되는 수열의 20번째 항까지의 합계
"""

# 문제 정답 출력
a = 0
b = 1
answer = 0
for i in range(20):
    # print(b, end=' ')
    answer += b
    a += 1
    b += a
print(f'\n<정답> : {answer}\n')

# 메서드 화

def day04():
    a = 0
    b = 1
    answer = 0
    for i in range(20):
        answer += b
        a += 1
        b += a
    return answer

print(f'<정답_메서드> : {day04()}')