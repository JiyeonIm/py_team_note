# 현재 나이트의 위치 입력받기
data = input()
# ord : unicode 반환 = ascii 코드 / ord('a')는 97
col = int(ord(data[0])) - int(ord('a')) + 1
row = int(data[1])

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2),(2, -1), (2, 1), (-1, 2), (1, 2)]

result = 0
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# 나는 0을 col로, 1을 row로 생각함
for step in steps:
  # 이동하고자 하는 위치 확인
  next_col = col + step[0]
  next_row = row + step[1]

  # 행 위치와 열 위치가 모두 1~8사이를 벗어나지 않을때 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1

print(result)
