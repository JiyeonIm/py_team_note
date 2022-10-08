# 시간 h 입력받기
h = int(input())

count = 0

# i는 0부터 h까지 1씩 증가하도록 함
# h=5 라면 0, 1, 2, 3, 4, 5
for i in range(h + 1):
  # 1시간 = 60분
  for j in range(60):
    # 1분 = 60초
    for k in range(60):
      # 매 시각에 3이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
