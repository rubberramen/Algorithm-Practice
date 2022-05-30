"""
# 문제
- 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

## 입력
- 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

## 출력
- 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
"""

# 성공

n = int(input())

nums_str = input()
nums_list = []

for i in nums_str:
    nums_list.append(int(i))

sum = 0
for j in nums_list:
    sum += j
print(sum)

"""
- 그런데 for문이 두개나 있음
- nums_list를 효율적으로 만들 수 있는 방법을 생각해 봐야
"""