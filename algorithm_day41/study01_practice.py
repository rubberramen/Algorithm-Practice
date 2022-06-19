"""<이것이 취업을 위한 코딩 테스트다 with 파이썬 ch.05 DFS/BFS>

## BFS : Breadth-First-Search 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- 선입선출 방식인 Que 자료구조를 이용하는 것이 정석
    - 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행함
- 알고리즘 동작 방식
    - 1) 탐색 시작 노드를 Que에 삽입하고 방문 처리를 한다.
    - 2) Que에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 Que에 삽입하고 방문 처리를 한다.
    - 3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

- BFS는 Que 자료구조에 기초한다는 점에서 구현이 간단
- 파이썬에서는 deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요
- 일반적인 경우, 실제 수행 시간은 DFS보다 좋은 편
"""

from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# visited 리스트 출력
print()
print(visited)