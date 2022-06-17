"""<이것이 취업을 위한 코딩 테스트다 with 파이썬 ch.05 DFS/BFS>

1. 스택(Stack)
2. 큐(Que)
3. 재귀 함수(Recursive Function)
"""

"""
# 03. 재귀 함수_Recursive Function
- 자기 자신을 다시 호출하는 함수
- 프랙털(Fracktal) 구조와 유사

## 재귀 함수의 종료 조건
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다.
- 자칫 종료 조건을 명시하지 않으면 함수가 무한 호출될 수 있다.

- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용
    - 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료

- 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있음
    - DFS가 대표적
"""

"""
# ex
def recursive_function():
    print('재귀 함수를 호출')
    recursive_function()

recursive_function()

'''
코드 실행하면 문자열이 무한히 출력
'''
"""

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 10:
        return

    print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료')

recursive_function(1)

print()

# 팩토리얼

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))