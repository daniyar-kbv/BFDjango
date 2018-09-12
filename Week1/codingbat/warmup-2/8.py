def array123(nums):
  one = 0
  two = 0
  three = 0
  for i in nums:
    if i == 1:
      one = 1
      continue
    if one == 1 and i == 2:
      two = 1
      continue
    elif i != 3:
      one = 0
      two = 0
    if one == 1 and two == 1 and i == 3:
      three = 1
      continue
    else:
      one = 0
      two = 0
      three = 0
  if one == 1 and two == 1 and three == 1: return True
  else: return False
