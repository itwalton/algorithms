##########################
# Randomized Selection
##########################
#   Description
#       Finds ith order statistic from unordered list by partitioning around random element and recursing over subset
#       Derived from Coursera's Divide & Conquer Algorithms by Tim Roughgarden
#
#   Algorithm
#       1. Choose pivot p from A uniformly at random
#       2. Order elements around the pivot, so that elements < pivot are on the left and elements >= pivot are on the right
#       3. If the pivot index is < requested ith order, traverse the right subarray
#       4. If the pivot index is > requested ith order, traverse the left subarray
#       5. If the pivot index is the ith order, return pivot
#
#   Runtime Complexity (worst case): O(n^2) [partitioning subroutine returns two lists of lengths 1 and n-1. Executes n subprocesses with n calculations]
#   Runtime Complexity (best case): O(n) [partitioning subroutine returns two lists of equal length]
#   Space Complexity: O(log(n))
##########################
import random

def partition(alist, start, end):
  # choose pivot at random
  random_pivot = random.randint(start, end)

  # swap the random element w/ the start element to start "ordered" segment
  alist[start], alist[random_pivot] = alist[random_pivot], alist[start]

  i = start

  # move elements < pivot to ordered section bounded by start and i
  for j in range(start+1, end+1):
    if alist[j] < alist[start]:
      i += 1
      alist[i], alist[j] = alist[j], alist[i]

  # swap the right-most element in ordered section with pivot, so that pivot remains middle-most element
  alist[start], alist[i] = alist[i], alist[start]

  # return pivot index
  return i

def randomized_selection(alist, i, start, end):
  # set has <= 1 element
  if start >= end:
    return alist[start]

  # partition around the random pivot
  pivot = partition(alist, start, end)

  # pivot was greater than ith order statistic, traverse left-side of alist
  if pivot + 1 > i:
    return randomized_selection(alist, i, start, pivot - 1)

  # pivot was less than ith order statistic, traverse right-side of alist
  elif pivot + 1 < i:
    return randomized_selection(alist, i, pivot + 1, end)

  # pivot is the ith order statistic
  else:
    return alist[pivot]
