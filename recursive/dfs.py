# DFS method
# param: graph, node v, 방문여부
def dfs(graph, v, visited):
  # 현재 노드 v 를 방문처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드 v와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    # 방문하지 않았다면 재귀적으로 호출
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드 번호대로 연결된 정보를 표현 (2차원 리스트)
graph = [
  [], # 1번 노드는 index 0이므로 사용하지 않음
  [2, 3, 8],
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

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
