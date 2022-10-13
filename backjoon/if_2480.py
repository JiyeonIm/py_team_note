a, b, c = map(int, input().split())

if a == b == c:
  reward = 10000 + (c * 1000)
elif a == b or a == c:
  reward = 1000 + (a * 100)
elif b == c:
  reward = 1000 + (b * 100)
else:
  i = max(a, b, c)
  reward = i * 100

print(reward)
