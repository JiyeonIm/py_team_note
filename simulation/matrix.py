# n 입력받기
n = int(input())

# 초기값
x, y = 1, 1

# 계획 입력받기
plans = input().split()

# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1] # L, R
dy = [-1, 1, 0, 0] # U, D

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  # 만약 공간을 벗어난다면 무시 - 부등호 조심해라..
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  # 이동 수행
  x, y = nx, ny

print(x, y)
