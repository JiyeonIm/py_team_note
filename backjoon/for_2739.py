# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# input : 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# output : 출력형식과 같게 N*1부터 N*9까지 출력한다.

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
