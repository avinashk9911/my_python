def kadanes(array):
  local_max=0
  global_max=-float("inf")
  n=0
  while n<len(array):
    local_max=max(array[n],array[n]+local_max)
    global_max=max(local_max,global_max)
    n+=1

  return global_max

array=[1,2,3,-2,5]
kadanes(array)
