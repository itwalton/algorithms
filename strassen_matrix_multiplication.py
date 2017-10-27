import numpy as np

def square_matrix_multiplication(matrixA, matrixB):
  n = len(matrixA) # assume square
  matrixC = [[0 for x in range(n)] for y in range(n)]

  # row in matrixA
  for i in range(0, n):
    row = list()

    # column in matrixB
    for j in range(0, n):
      matrixC[i][j] = 0

      # column in matrixA; row in matrixB
      for k in range(0, n):
        matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

  return matrixC

def matrix_add(a, b):
  return [[ea+eb for ea, eb in zip(*rowpair)] for rowpair in zip(a, b)]

def matrix_subtract(a, b):
  return [[ea-eb for ea, eb in zip(*rowpair)] for rowpair in zip(a, b)]

def join_horiz(a, b):
    return [rowa + rowb for rowa, rowb in zip(a,b)]

def join_vert(a, b):
    return a+b

def recursive_square_matrix_multiplication(matrixA, matrixB):
  n = len(matrixA)
  matrixC = [[0 for x in range(n)] for y in range(n)]

  if n == 1:
    matrixC[0][0] = matrixA[0][0] * matrixB[0][0]
  else:
    a = [[col for col in row[:len(row)//2]] for row in matrixA[:len(matrixA)//2]]
    b = [[col for col in row[len(row)//2:]] for row in matrixA[:len(matrixA)//2]]
    c = [[col for col in row[:len(row)//2]] for row in matrixA[len(matrixA)//2:]]
    d = [[col for col in row[len(row)//2:]] for row in matrixA[len(matrixA)//2:]]
    e = [[col for col in row[:len(row)//2]] for row in matrixB[:len(matrixB)//2]]
    f = [[col for col in row[len(row)//2:]] for row in matrixB[:len(matrixB)//2]]
    g = [[col for col in row[:len(row)//2]] for row in matrixB[len(matrixB)//2:]]
    h = [[col for col in row[len(row)//2:]] for row in matrixB[len(matrixB)//2:]]
    ae = recursive_square_matrix_multiplication(a,e)
    bg = recursive_square_matrix_multiplication(b,g)
    af = recursive_square_matrix_multiplication(a,f)
    bh = recursive_square_matrix_multiplication(b,h)
    ce = recursive_square_matrix_multiplication(c,e)
    dg = recursive_square_matrix_multiplication(d,g)
    cf = recursive_square_matrix_multiplication(c,f)
    dh = recursive_square_matrix_multiplication(d,h)

    matrixC = join_vert(join_horiz(matrix_add(ae, bg), matrix_add(af,bh)), join_horiz(matrix_add(ce,dg), matrix_add(cf,dh)))

  return matrixC

##########################
# Strassens Matrix Multiplication
##########################
#   Algorithm:
#       1. Divide the input matrices A and B and output matrix C into n/2 * n/2 submatrices
#       2. Create 10 matrices S1, S2, ..., S10 each with n/2 * n/2 and the sum or difference of two matrices created in Step #1
#       3. Using the submatrices from Step #1 & #2, recursively compute 7 matrix products P1, P2, ..., P7 each of length n/2 * n/2.
#       4. Compute the desired submatrices C11, C12, C21, C22 (4 quatrices of output)
#
#   Runtime Complexity: O(n^log7)
##########################
def strassan_matrix_multiplication(matrixA, matrixB):
  n = len(matrixA)

  if n is 1:
      return [[matrixA[0][0] * matrixB[0][0]]]
  else:
      newSize = len(matrixA)//2

      # initializing the new sub-matrices
      a11 = [[col for col in row[:newSize]] for row in matrixA[:newSize]]
      a12 = [[col for col in row[newSize:]] for row in matrixA[:newSize]]
      a21 = [[col for col in row[:newSize]] for row in matrixA[newSize:]]
      a22 = [[col for col in row[newSize:]] for row in matrixA[newSize:]]
      b11 = [[col for col in row[:newSize]] for row in matrixB[:newSize]]
      b12 = [[col for col in row[newSize:]] for row in matrixB[:newSize]]
      b21 = [[col for col in row[:newSize]] for row in matrixB[newSize:]]
      b22 = [[col for col in row[newSize:]] for row in matrixB[newSize:]]

      p1 = strassan_matrix_multiplication(matrix_add(a11, a22), matrix_add(b11, b22)) # p1 = (a11+a22) * (b11+b22)
      p2 = strassan_matrix_multiplication(matrix_add(a21, a22) , b11)  # p2 = (a21+a22) * (b11)
      p3 = strassan_matrix_multiplication(a11, matrix_subtract(b12, b22))  # p3 = (a11) * (b12 - b22)
      p4 = strassan_matrix_multiplication(a22, matrix_subtract(b21, b11))   # p4 = (a22) * (b21 - b11)
      p5 = strassan_matrix_multiplication(matrix_add(a11, a12), b22)  # p5 = (a11+a12) * (b22)
      p6 = strassan_matrix_multiplication(matrix_subtract(a21, a11), matrix_add(b11, b12)) # p6 = (a21-a11) * (b11+b12)
      p7 = strassan_matrix_multiplication(matrix_subtract(a12, a22), matrix_add(b21, b22)) # p7 = (a12-a22) * (b21+b22)

      # calculating c21, c21, c11 e c22:
      c11 = matrix_subtract(matrix_add(matrix_add(p1, p4), p7), p5) # c11 = p1 + p4 - p5 + p7
      c12 = matrix_add(p3, p5) # c12 = p3 + p5
      c21 = matrix_add(p2, p4)  # c21 = p2 + p4
      c22 = matrix_subtract(matrix_add(matrix_add(p1, p3), p6), p2) # c22 = p1 + p3 - p2 + p6

      # Grouping the results obtained in a single matrix:
      return join_vert(join_horiz(c11, c12), join_horiz(c21, c22))
