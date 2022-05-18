"""
<문제> : 진법변환
    10진수를 2진수로 변환하기
"""

# 테스트2 : 리스트를 숫자로 변환

n = 13
answer_list = []

while n // 2 > 0:
    a = n % 2   # a == 1
    # print('나머지 :', a)
    answer_list.append(a) #
    # print(answer_list)
    n = n // 2
    # print('내려오는 수 : ',n)
    # print()
answer_list.append(n)

print(answer_list)
print()


# 리스트 -> 숫자
answer_num = 0                     # 최종 결과 변수
temp = 0                           # 지수

for i in answer_list:
    print(i)                       # 리스트 요소 차례로 출력
    answer_num += (10**temp) * i   # 숫자로 변환
    temp += 1                      # 지수 + 1

print()
print('정답 : ', answer_num)