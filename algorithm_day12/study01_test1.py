"""
<문제> : 진법변환
    10진수를 2진수로 변환하기
"""

# 테스트1 : 리스트로 출력

n = 13
answer_list = []

while n // 2 > 0:             # 몫이 0보다 클때까지 : 1
    a = n % 2                 # 첫 나머지
    print('나머지 :', a)
    answer_list.append(a)     # 리스트에 추가
    print(answer_list)
    n = n // 2                # 몫
    print('내려오는 수 : ',n)
    print()
answer_list.append(n)         # 최종 숫자 리스트에 추가

print('-'*30)
print(answer_list)            # 리스트 출력 : 이진법 순서
print('-'*30)

# 검산
original_num = (2**0) * answer_list[0] + (2**1) * answer_list[1] + (2**2) * answer_list[2] + (2**3) * answer_list[3]
print('원래 수 : ', original_num)