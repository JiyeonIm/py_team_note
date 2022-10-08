# 큐 구현 위해 deque 라이브러리 사용
from collections import deque

# bfs 구현
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    # queue에서 현재 위치 꺼내오기
    x, y = queue.popleft()

    # 현재 위치에서 4방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      # 벽=값이 0인 경우 무시
      if graph[nx][ny] == 0:
        continue

      # 해당 노드 처음 방문 하는 경우에만 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
        
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]


# n, m을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트로 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 4가지 방향 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행한 결과 출력
print(bfs(0, 0))
