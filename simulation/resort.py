data = str(input())

num = 0
digit = []

for i in range(len(data)):
  if data[i].isnumeric():
    num += int(data[i])
  else:
    digit.append(data[i])

digit.sort()
digit.append(str(num))

print(''.join(digit))



# --------------------------
# 답안
data = input()

result = []
value = 0

# 문자 하나씩 확인
for x in data:
  # 알파벳인 경우 리스트에
  if x.isalpha():
    result.appned(x)
  # 숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재할 때 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
