# 22-05-04(수)
# 수열01 : 1+2+3+4+ ... +100까지의 합계

num = 0
answer = 0

for i in range(100):
    num += 1
    answer += num

print('\n문제 : 1+2+3+4+ ... +100 까지의 합계 구하기')
print(f'정답 : {answer}')
