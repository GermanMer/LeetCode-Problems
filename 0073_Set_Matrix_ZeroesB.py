# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Primero, identificamos las filas y columnas que necesitan ser configuradas a cero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Luego, configuramos las filas a cero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Y finalmente, configuramos las columnas a cero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0

# Example 1:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
Solution().setZeroes(matrix)
print(matrix)

# Example 2:
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Solution().setZeroes(matrix)
print(matrix)
