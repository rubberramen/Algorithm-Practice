"""
# 문제 : A+B-3_백준 10950
    - 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력
    - 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    - 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력
    - 각 테스트 케이스마다 A+B를 출력한다.
"""

# 구글 검색 : for _ in range(t)

t = int(input())                        # T값 입력받음

for _ in range(t):                      # t번 반복 : underscore 활용(값을 무시하고 싶은 경우)
    n1, n2 = map(int, input().split())  # 두 개의 숫자를 입력받음
    print(n1 + n2)                      # 합산 출력

"""
<언더 스코어 활용> : https://mingrammer.com/underscore-in-python/
- 파이썬에서는 언더스코어(underscore)의 용법이 다앙하다.
- 그 중에, '값을 무시하고 싶은 경우'에 사용할 수도 있다.
"""