"""
<문제> : 진법변환
    10진수를 2진수로 변환하기
"""

# 메서드

def day12(n):
    answer_list = []
    while n // 2 > 0:
        a = n % 2  # a == 1
        answer_list.append(a)  #
        n //= 2
    answer_list.append(n)

    answer_num = 0
    temp = 0

    for i in answer_list:
        answer_num += (10 ** temp) * i
        temp += 1

    return answer_num

# 정답 출력
n1 = int(input('이진법으로 변환할 수 입력 : '))
n = n1
print(f'{n1}을 이진법으로 변환 : {day12(n)}')