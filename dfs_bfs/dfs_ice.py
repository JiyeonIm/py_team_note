# DFS 로 graph[x][y]의 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 현재 위치가 범위를 벗어나면 false로 return
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드(위치)의 값이 0이면(방문하지 않았다면) 해당 노드를 방문처리함
    # 1이면 방문한걸로 칠테니 false로 return 하고 끝
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 연결된 노드를 dfs 재귀 호출
        # return 값을 사용하지 않으니 그냥 방문처리를 위한 목적으로 쓰임
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        # 상,하,좌,우 다 움직여서 해당 위치를 계속 호출하고, 모두 다 돌면 True?
        # 현재 위치에 대해서 처음 dfs가 수행된 것이기 때문에
        return True
    return False


# col n, row m
# n, m을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트로 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # dfs return 값이 True 일때 result 증가
        # 현재 위치에서 DFS 수행
        # 처음 위치에서 상하좌우 다 돌고 방문 처리 후 돌아 오면 result가 증가
        if dfs(i, j):
            result += 1

print(result)

# 이걸 어떻게 풀어?
