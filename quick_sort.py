#################
# Quicksort
#################
#   Description
#       Sorts array of elements by sorting a single element and recursing over the remaining subarrays on either side
#       Derived from Coursera's Divide & Conquer Algorithms by Tim Roughgarden
#
#   Algorithm
#       1. Choose pivot p from A uniformly at random
#       2. Order elements around the pivot, so that elements < pivot are on the left and elements >= pivot are on the right
#       3. Recurse over the left/right subarrays
#
#   Runtime Complexity (worst case): O(n^2) [partitioning subroutine returns two lists of lengths 1 and n-1. Executes n subprocesses with n calculations]
#   Runtime Complexity (best case): O(nlogn) [partitioning subroutine returns two lists of equal length]
#   Space Complexity: O(log(n))
###############
import random

def partition(alist, start, end):
  # choose pivot at random - much less likely to yield quadratic runtime
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

  return i

def quick_sort(alist, start, end):
  # set has <= 1 element
  if start >= end:
    return alist

  # sort a random element, returning its index
  pivot = partition(alist, start, end)

  # traverse over elements < pivot
  quick_sort(alist, start, pivot - 1)

  # traverse over elements > pivot
  quick_sort(alist, pivot + 1, end)

  return alist
