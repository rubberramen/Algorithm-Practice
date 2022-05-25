"""
<언더 스코어 활용> : https://mingrammer.com/underscore-in-python/
- 파이썬에서는 언더스코어(underscore)의 용법이 다앙하다.
- 그 중에, '값을 무시하고 싶은 경우'에 사용할 수도 있다.

- _는 어떤 특정값을 무시하기 위한 용도로 사용되기도 한다.
- 값이 필요하지 않거나, 사용되지 않는 감ㅅ을 _에 할당한다.
"""

# 언패킹시 특정값을 무시
x, _, y = (1, 2, 3) # x = 1, y = 3
print(x, y)
print()

# 인덱스 무시
for _ in range(5):
    print('python!', end=' ')
print()

# 상황에 따라 요긴하게 쓸 수도 있겠음
