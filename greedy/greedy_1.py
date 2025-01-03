n, k = map(int, input().split())

result = 0

while True:
  # n을 k로 나눈 몫에 k를 곱함
  # n이 k로 나누어 떨어지지 않을때, 나누어 떨어질 수 있는 가장 가까운 수를 찾을 수 있음 WOW
  # 따라서, n에서 1을 빼는 과정을 몇 번 반복해서 k로 나누어 떨어지는 target의 값까지 만들수 있는지 알 수 있음  
  target = (n // k) * k
  # 1을 빼는 회수를 모조리 계산해서 넣어버림
  result += (n - target)   
  # 그리고 n이 target이 되도록 만듬
  n = target
  # 더이상 나눌 수 없을 때 반복문 탈출
  if n < k:
    break

  # 아니라면 k로 나눈 값을 n으로..
  n //= k
  result +=1

# n이 1보다 크다면 마지막 1이 될때까지 1씩 빼기
result += (n - 1)

print(result)

# 이렇게 하면 100만 단위의 큰 숫자들도 시간 복잡도를 줄일 수 있음
# 예시 답안 25 5 -> 2 / 25 3 -> 3
