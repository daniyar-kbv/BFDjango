def array_front9(nums):
  cnt = 0
  for i in nums:
    cnt += 1
    if i == 9: return True
    if cnt == 4: break
  return False
