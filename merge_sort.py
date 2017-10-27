def merge_sort(alist):
  if len(alist) == 1:
    return alist

  half = len(alist)//2
  left_list = alist[:half]
  right_list = alist[half:]

  merge_sort(left_list)
  merge_sort(right_list)

  i = 0
  j = 0
  k = 0
  while (i < len(left_list)) & (j < len(right_list)):
    if left_list[i] < right_list[j]:
      alist[k] = left_list[i]
      i = i + 1
    else:
      alist[k] = right_list[j]
      j = j + 1
    k = k + 1

  while i < len(left_list):
    alist[k] = left_list[i]
    i = i + 1
    k = k + 1

  while j < len(right_list):
    alist[k] = right_list[j]
    j = j + 1
    k = k + 1

  return alist
