# 22.10.13 푼거
# 코드 길이 225
h, m = map(int, input().split())

if h == 0:
    h = 24
else:
    h = h

if m < 45:
    m2 = h * 60 + m
    h2 = (m2 - 45)//60
    m2 = (m2 - 45)%60
    print(h2, m2)
else:
    if h == 24:
        h = 0

    print(h, m - 45)

    
# 3년전에 푼거
# 코드 길이 258
user = input()
a = int(user.split(' ')[0])
b = int(user.split(' ')[1])

if b >= 45:
    print(str(a) + ' ' + str(b-45))
elif b < 45 and b < 60:
    if a < 1:
        print(str(a+23) + ' ' + str(b+60-45))
    else:
        print(str(a-1) + ' ' + str(b+60-45))

        
# 합쳐서 다시 푼거
# 이게 좀 더 빠름 메모리는 같음
# 코드 길이 186
h, m = map(int, input().split())

if m >= 45:
  print(str(h), str(m - 45))
else:
  if h == 0:
    print(str(h) + 23, str(m + 15))
  else:
    print(str(h - 1), str(m + 15))
    
# 코드 길이 133 제일 
h, m = map(int, input().split())

if m >= 45:
  print(h, m - 45)
else:
  if h == 0:
    h = 24
  else:
    h = h
  print(h-1, m + 15)
