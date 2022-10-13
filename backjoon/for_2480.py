# 22.10.13
n = int(input())

for j in range(1, 10):
  print(n, '*', j, '=', n*j)


# 3년전
a = int(input())
i = 1
while True:
    b = a*i
    print(str(a) + ' * ' + str(i) + ' = ' + str(b))
    i += 1
    if i > 9:
        break
