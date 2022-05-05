# 22-05-05(목)
# 수열02-3 : (-1)×2×(-3)×4×(-5)× ··· ×100의 합계

num = 0
answer = 1

for i in range(100):
    num += 1
    if num % 2 != 0:
        answer *= (-1) * num
    else:
        answer *= num

print('\n문제 : (-1)×2×(-3)×4×(-5)× ··· ×100의 합계')
print(f'정답 : {answer : .4e}')

'''
- 문자열 f-formatting 확실히 잡음
- 소숫점 표현할 시, f vs e -> 확인 필요
'''