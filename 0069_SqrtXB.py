# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Manejo especial para 0 y 1

        left, right = 2, x // 2  # Establecer límites para la búsqueda binaria

        while left <= right:
            mid = left + (right - left) // 2  # Evitar desbordamiento

            if mid * mid == x:
                return mid  # Si encontramos la raíz exacta
            elif mid * mid < x:
                left = mid + 1  # Buscar en la mitad derecha
           else:
                right = mid - 1  # Buscar en la mitad izquierda

        return right  # En este punto, right es la raíz entera redondeada hacia abajo

# Example 1:
x = 4
# Output: 2
print(Solution().mySqrt(x))

# Example 2:
x = 8
# Output: 2
print(Solution().mySqrt(x))
