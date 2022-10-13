# 도대체 왜 틀리지????????
h, m = map(int, input().split())
cook = int(input())

if cook >= 60:
  h += 1
  m2 = cook - 60 + m
else:
  m2 = m + cook

if m2 >= 60:
  h += 1
  m2 = m2 - 60

if h > 23:
  h = 0

print(h, m2)

# 아무래도 h=0 이부분이 틀린듯.. h-24 였으면...^^
# 아닌듯 += 1 이것도 틀린듯 ㅋㅋㅋㅋㅋㅋㅋㅋ

# 이건 
h, m = map(int, input().split())
cook = int(input())

if m + cook >= 60:
  h += (m + cook) // 60
  m += cook % 60
else:
  m += cook
  
if m >= 60:
  m -= 60
  
if h > 23:
  h -= 24

print(h, m)
