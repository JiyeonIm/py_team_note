def gcd(a, b):
  # 나머지가 0일때, 즉 배수일때는 b가 최대공약수
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(192, 162))
