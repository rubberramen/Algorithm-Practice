"""<day32_백준 14490_백대열>
# 문제
- 대열이는 욱제의 친구다.

    - “야 백대열을 약분하면 뭔지 알아?”
    - “??”
    - “십대일이야~ 하하!”
- n:m이 주어진다. 욱제를 도와주자. (...)

## 입력
- n과 m이 :을 사이에 두고 주어진다. (1 ≤ n, m ≤ 100,000,000)

## 출력
- 두 수를 최대한으로 약분하여 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/14490
"""

def GCD(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
            break

n, m = map(int, input().split(':'))
k = GCD(n, m)
print(f'{int(n/k)}:{int(m/k)}')