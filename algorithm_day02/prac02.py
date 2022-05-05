# 22-05-05(목)
# 수열02-2 : 1-2+3-4+5-6+ ... +99의 합계

num = 0
answer = 0

for i in range(99):
    num += 1
    if num % 2 != 0:
        answer += num
    else:
        answer -= num

print('\n문제 : 1-2+3-4+5-6+ ... +99의 합계')
print(f'정답 : {answer}')
