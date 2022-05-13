"""
<문제> : 약수 구하기
    정수를 입력 받아, 약수를 구해 출력
"""

def day10(n):
    list_answer = []               # 약수를 담을 빈 리스트 생성

    for i in range(1, n+1):        # 1~n까지 약수인지 확인
        if n % i == 0:             # 약수면
            list_answer.append(i)  # 리스트에 추가
    return list_answer             # 정답 리스트 리턴

n = int(input('숫자 입력 : '))
print(f'{n}의 약수 : {day10(n)}')