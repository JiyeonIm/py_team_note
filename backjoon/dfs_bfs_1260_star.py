"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

input : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

output : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

"""
# 더 짧은 코드
from collections import deque

# dfs part
def dfs(graph, s, visit):
  visit[s] = True
  print(s, end=' ')
  for i in graph[s]:
    if not visit[i]:
      dfs(graph, i, visit)

      
# bfs part
def bfs(graph, s, visit):
  visit[s] = True
  queue = deque([s])
  
  while queue:
    q = queue.popleft()
    print(q, end=' ')
    for i in graph[q]:
      if not visit[i]:
        visit[i] = True
        queue.append(i)
  

# input part
n, e, s = map(int, input().split())

# graph part
graph = {x: [] for x in range(1, n + 1)}

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향이므로


# 작은 숫자부터 순서대로 들어가므로 sort
for i in graph:
    graph[i].sort()

dfs(graph, s, [False] * (n + 1))
print()
bfs(graph, s, [False] * (n + 1))

# ----------
# 처음 맞은 코드

from collections import deque

# dfs
def dfs(graph, start, visit):
    visit[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visit[i]:
            dfs(graph, i, visit)


# bfs
def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    
    while queue:
      q = queue.popleft()
      print(q, end=" ")
      for i in graph[q]:
        if not visit[i]:
          queue.append(i)
          visit[i] = True


# graph part
nodes, edges, start = map(int, input().split())

graph = {x: [] for x in range(1, nodes + 1)}

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향이므로

for i in graph:
    graph[i].sort()

dfs(graph, start, [False] * (nodes + 1))
print()
bfs(graph, start, [False] * (nodes + 1))

