n = input()
x = list(map(int, input().split()))

# 오름차순 정렬 이후 공포도가 낮은 모험가부터 하나씩 확인
x.sort()

group = 0 # 현재 그룹에 포함된 모험가 수
result = 0 # 총 그룹의 수

for i in x: # 공포도를 낮은 것 부터 하나씩 확인하며
  group += 1 # 현재 그룹에 해당 모험가 포함 (i번째)
  if group >= i: # 현재 그룹의 포함된 모험가 수가 현재의 공포도 이상이면 그룹 끝
    result += 1 # 그룹의 수가 하나 늘고
    group = 0 # 현재 그룹에 포함된 모험가 수 초기화

print(result)
