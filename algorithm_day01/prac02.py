# 22-05-04(수)
# 수열01-2 : 1+3+5+7+...+99 까지의 합계

num = 0
answer = 0

for i in range(100):
    num += 1
    if num % 2 != 0:
        answer += num
    else:
        pass

print('\n문제 : 1+3+5+7+...+99 까지의 합계 구하기')
print(f'정답 : {answer}')
