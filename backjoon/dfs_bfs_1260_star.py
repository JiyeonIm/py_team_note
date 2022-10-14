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

