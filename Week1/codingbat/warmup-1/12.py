def front3(str):
  if len(str) <= 3:
    return str + str + str
  else:
    new = str[0:3]
    return new + new + new
