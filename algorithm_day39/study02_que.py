"""<이것이 취업을 위한 코딩 테스트다 with 파이썬 ch.05 DFS/BFS>

1. 스택(Stack)
2. 큐(Que)
3. 재귀 함수(Recursive Function)
"""

"""
# 02. Que
- Que는 대기 줄에 비유할 수 있음
- 선입선출(First In First Out)
"""

from collections import deque

# Queue 구현을 위해 deque 라이브러리 사용
queue = deque()
print(queue)

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)

queue.popleft()
print(queue)

queue.append(1)
queue.append(4)
print(queue)

queue.popleft()
print(queue, end = '\n\n')     # 먼저 들어온 순서대로 출력

queue.reverse()                # 다음 출력을 위해 역순으로 바꾸기
print(queue)                   # 나중에 들어온 원소부터 출력

# deque 객체를 리스트 자료형으로 변경
list_from_deque = list(queue)
list_from_deque