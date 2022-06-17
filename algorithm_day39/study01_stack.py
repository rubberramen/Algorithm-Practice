"""<이것이 취업을 위한 코딩 테스트다 with 파이썬 ch.05 DFS/BFS>

1. 스택(Stack)
2. 큐(Que)
3. 재귀 함수(Recursive Function)
"""

"""
# 01. Stack
- Stack는 박스 쌓기에 비유할 수 있음
- 선입후출(First In Last Out) or 후입선출(Last In First Out)
- 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없음
- 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작
- append()메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop() 메서드는 리스트의 가장 뒤쪽에서 데이터를 꺼냄
"""

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)
stack.pop()

print(stack)         # 최하단 원소부터 출력
print(stack[::-1])   # 최상단 원소부터 출력