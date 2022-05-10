"""
<문제>
    1+2+4+7+11+16+22+...의 순서로 나열되는 수열의 20번째 항까지의 합계
"""

# 메서드 확장 : 사용자에게 입력받은 n을 파라미터로

def algo_05_extend(n):         # 파라미터 추가
    a = 0
    b = 1
    answer = 0
    for i in range(n):
        answer += b
        a += 1
        b += a
    return answer

n = int(input("n 입력 : "))    # 사용자에게 입력받도록
print(f'수열 1,2,4,7,11,16,22,...의 n번째 항까지의 합계 : {algo_05_extend(n)}')