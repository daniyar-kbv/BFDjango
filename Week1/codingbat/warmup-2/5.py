def last2(str):
  cnt = 0
  last = str[len(str) - 2: len(str)]
  for i in range(len(str) - 2):
    if (str[i:i+2] == last): cnt += 1
  return cnt
