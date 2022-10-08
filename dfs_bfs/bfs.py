from collections import deque

# BFS method
def bfs(graph, start, visited):
  # 첫번째 과정부터!
  # 시작 노드를 queue에 넣어줌
  queue = deque([start])
  # 현재 노드 방문 처리
  visited[start] = True
  
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    # 가장 먼저 들어왔던 원소 뽑긔
    v = queue.popleft()
    print(v, end=' ')
    # 그 꺼낸 노드의 방문하지 않은 인접한 노드들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


# 각 노드 번호대로 연결된 정보를 표현 (2차원 리스트)
# 총 9개의 정보를 표현
graph = [
  [], # 0번 노드는 index 0이므로 사용하지 않음
  [2, 3, 8], # 1번 노드의 연결 노드들
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 1부터 8번까지의 노드이므로 0번 index를 사용하지 않게 하나 더 큰 숫자를 곱해줌
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
