"""<day37_백준 2447_별 찍기-10>

# 문제
- 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

- '***'
- '* *'
- '***'

- N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

## 입력
- 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

## 출력
- 첫째 줄부터 N번째 줄까지 별을 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/2447
"""

def stars(star_list):
    matrix = []
    for i in range(3 * len(star_list)):
        if i // len(star_list) == 1:
            matrix.append(star_list[i % len(star_list)] + " " * len(star_list) + star_list[i % len(star_list)])
        else:
            matrix.append(star_list[i % len(star_list)] * 3)
    return(list(matrix))

star_original = ["***", "* *", "***"]
star_list = star_original

n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star_list = stars(star_list)
for i in star_list:
    print(i)