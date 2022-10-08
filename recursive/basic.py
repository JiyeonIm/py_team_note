def recursive_function(i):
  # 15번 호출했을 때 종료하도록
  if i == 15:
    return
  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수 호출')
  recursive_function(i+1)
  print(i, '번째 재귀함수 종료')


recursive_function(1)
