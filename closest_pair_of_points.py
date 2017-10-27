##########################
# Closest Pair of Points
##########################
#   Description
#       Determine the closest pair of two-dimensional points
#       Derived from Coursera's Divide & Conquer Algorithms by Tim Roughgarden
##########################

from math import sqrt

def calc_euclidean_distance(pointA, pointB):
  return sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)

##########################
# Brute Force Method
##########################
#   Algorithm
#       1. Iterate over every single set of points
#       2. Return closest pair in set
#
#   Runtime Complexity: O(n^2)
##########################
def closest_pair_brute_force(P):
  best_distance = 999
  best_pair = None
  for i in range(len(P)):
    for j in range(i + 1, len(P)):
      distance = calc_euclidean_distance(P[i], P[j])

      if distance < best_distance:
        best_distance = distance
        best_pair = [P[i], P[j]]

  return best_pair

##########################
#   Divide & Conquer Method: O(nlogn)
##########################
#   Algorithm
#
#   Runtime Complexity: O(nlogn)
##########################
def sort_points_by_axis(P, byX=False):
  if len(P) is 1:
    return P

  left_points = sort_points_by_axis(P[:len(P)//2])
  right_points = sort_points_by_axis(P[len(P)//2:])

  i = 0
  j = 0
  k = 0

  while i < len(left_points) and j < len(right_points):
    if byX is True:
      if left_points[i][0] < right_points[j][0]:
        P[k] = left_points[i]
        i = i + 1
        k = k + 1
      else:
        P[k] = right_points[j]
        j = j + 1
        k = k + 1
    else: # pos is 'y'
      if left_points[i][1] < right_points[j][1]:
        P[k] = left_points[i]
        i = i + 1
        k = k + 1
      else:
        P[k] = right_points[j]
        j = j + 1
        k = k + 1

  while i < len(left_points):
    P[k] = left_points[i]
    i = i + 1
    k = k + 1

  while j < len(right_points):
    P[k] = right_points[j]
    j = j + 1
    k = k + 1

  return P

def find_closest_pair_in_points(Px, Py):
  best_pair = None
  best_distance = 999
  for i in range(len(Px)):
    for j in range(i + 1, len(Py)):
      if (Px[i] == Py[j]) and (Px[i] == Py[j]):
        continue

      distance = calc_euclidean_distance(Px[i], Py[j])

      if distance < best_distance:
        best_distance = distance
        best_pair = [Px[i], Py[j]]

  return best_pair

def find_closest_split_pair(Px, Py, delta):
  median_x = Px[len(Px)//2][0]
  Sy = [ coord for coord in Py if median_x - delta <= coord[0] <= median_x + delta  ]

  best_pair = None
  best_distance = 999
  for i in range(len(Sy)):
    for j in range(i + 1, min(i+7, len(Sy))):
      distance = calc_euclidean_distance(Sy[i], Sy[j])
      if distance < best_distance:
        best_distance = distance
        best_pair = [Sy[i], Sy[j]]

  return best_pair

def closest_pair(Px, Py):
  if len(Px) <= 3:
    return find_closest_pair_in_points(Px, Py)

  Q = Px[len(Px)//2:]
  Qx = sort_points_by_axis(Q, True)
  Qy = sort_points_by_axis(Q, False)

  R = Px[:len(Px)//2]
  Rx = sort_points_by_axis(R, True)
  Ry = sort_points_by_axis(R, False)

  left_pair = closest_pair(Qx, Qy)
  left_distance = calc_euclidean_distance(left_pair[0], left_pair[1])

  right_pair = closest_pair(Rx, Ry)
  right_distance = calc_euclidean_distance(right_pair[0], right_pair[1])

  best_pair = None
  best_distance = None
  if left_distance < right_distance:
    best_pair = left_pair
    best_distance = left_distance
  else:
    best_pair = right_pair
    best_distance = right_distance

  split_pair = find_closest_split_pair(Px, Py, best_distance)
  if (split_pair is None) or best_distance < calc_euclidean_distance(split_pair[0], split_pair[1]):
    return best_pair

  return split_pair
