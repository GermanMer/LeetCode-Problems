# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []

        for i in range(n):
            row = []
            for x in range(n):
                row.append(0)
            matrix.append(row)

        num = 1
        top = 0
        right = n - 1
        bottom = n - 1
        left = 0

        while top <= bottom and left <= right:
            # Mover hacia la derecha
            for a in range(left, right + 1):
                matrix[top][a] = num
                num += 1
            top += 1

            # Mover hacia la abajo
            for b in range(top, bottom + 1):
                matrix[b][right] = num
                num += 1
            right -= 1

            # Mover hacia la izquierda
            if top <= bottom:  # Verificar que aún hay filas
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = num
                    num += 1
                bottom -= 1

            # Mover hacia la arriba
            if left <= right:  # Verificar que aún hay columnas
                for d in range(bottom, top - 1, -1):
                    matrix[d][left] = num
                    num += 1
                left += 1

        return matrix

# Example 1:
n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
print(Solution().generateMatrix(n))

# Example 2:
n = 1
# Output: [[1]]
print(Solution().generateMatrix(n))
