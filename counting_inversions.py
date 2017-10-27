def count_inversions_brute_force(alist):
  inversion_count = 0
  for idx, val in enumerate(alist):
    for idx2, val2 in enumerate(alist[:idx + 1]):
      if alist[idx] < alist[idx2]:
        inversion_count = inversion_count + 1

  return inversion_count

##########################
# Divide & Conquer Strategy
##########################
#   Algorithm

#   Runtime Complexity: O(nlogn)
##########################
def count_inversions(alist):
  output = alist
  output = dict()
  output['inversion_count'] = 0
  output['list'] = alist

  if len(alist) > 1:
    half = len(alist)//2
    left_list = alist[:half]
    right_list = alist[half:]

    left_dict = count_inversions(left_list)
    right_dict = count_inversions(right_list)

    output['inversion_count'] = left_dict['inversion_count'] + right_dict['inversion_count']

    i = 0
    j = 0
    k = 0
    while i < len(left_dict['list']) and j < len(right_dict['list']):
      if left_dict['list'][i] < right_dict['list'][j]:
        output['list'][k] = left_dict['list'][i]
        k = k + 1
        i = i + 1
      else:
        output['list'][k] = right_dict['list'][j]

        # magic happens here; when a right element is added, all of the remaining elements in the left array are inversions
        output['inversion_count'] = output['inversion_count'] + len(left_dict['list']) - i
        k = k + 1
        j = j + 1

    while i < len(left_list):
      output['list'][k] = left_dict['list'][i]
      k = k + 1
      i = i + 1

    while j < len(right_list):
      output['list'][k] = right_dict['list'][j]
      k = k + 1
      j = j + 1

  return output
