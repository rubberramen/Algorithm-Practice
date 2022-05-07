def sum_n(n):
    num = 0
    answer = 0
    for i in range(n):
        num += 1
        answer += num
    return answer

print(f'1부터 100까지의 합 : {sum_n(100)}')
