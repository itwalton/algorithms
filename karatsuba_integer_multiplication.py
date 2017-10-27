def original_karatsuba_recursion(num1, num2):
  if (len(str(num1)) == 1) or (len(str(num2)) == 1):
    return num1 * num2

  m = max(len(str(num1)), len(str(num2)))
  m2 = m // 2

  high1 = num1 // 10**(m2)
  low1 = num1 % 10**(m2)

  high2 = num2 // 10**(m2)
  low2 = num2 % 10**(m2)

  ac = original_karatsuba_recursion(high1, high2)
  ad = original_karatsuba_recursion(high1, low2)
  bc = original_karatsuba_recursion(low1, high2)
  bd = original_karatsuba_recursion(low1, low2)

  return (ac * 10**(2*m2)) + (10**(m2) * (ad + bc)) + bd

def optimized_karatsuba_recursion(num1, num2):
  if (len(str(num1)) == 1) or (len(str(num2)) == 1):
    return num1 * num2

  m = max(len(str(num1)), len(str(num2)))
  m2 = m // 2

  high1 = num1 // 10**(m2)
  low1 = num1 % 10**(m2)

  high2 = num2 // 10**(m2)
  low2 = num2 % 10**(m2)

  z1 = optimized_karatsuba_recursion((low1 + high1), (low2 + high2))
  z0 = optimized_karatsuba_recursion(high1, high2)
  z2 = optimized_karatsuba_recursion(low1, low2)

  return (z0 * 10**(2*m2)) + (10**(m2) * (z1 - z0 - z2)) + z2
