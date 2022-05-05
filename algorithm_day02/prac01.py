# 22-05-05(목)
# 수열02 : 1-2+3-4+5-6+ ... +99-100의 합계

num = 0
answer = 0

for i in range(100):
    num += 1
    if num % 2 != 0:
        answer += num
    else:
        answer -= num

print('\n문제 : 1-2+3-4+5-6+ ... +99-100의 합계')
print(f'정답 : {answer}')
