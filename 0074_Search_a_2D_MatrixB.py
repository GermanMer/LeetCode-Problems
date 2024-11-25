# You are given an m x n integer matrix matrix with the following two properties:
    # Each row is sorted in non-decreasing order.
    # The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# Enfoque de búsqueda binaria. (Dado que el problema establece que la matriz tiene filas ordenadas y que el primer elemento de cada fila es mayor que el último de la fila anterior, se puede tratar la matriz como un único arreglo unidimensional).
    # Definir los límites: Inicializa dos variables, left y right, para representar los índices del inicio y el final del "arreglo" virtual que representa la matriz.
    # Búsqueda binaria: Utiliza un bucle que continúe mientras left sea menor o igual a right. En cada iteración, calcula el índice medio mid, y determina la posición correspondiente en la matriz (fila y columna) usando la división y el módulo.
    # Comparación: Compara el valor en la posición mid con el target. Si son iguales, retorna True. Si el valor es menor que target, ajusta left para que sea mid + 1. Si es mayor, ajusta right a mid - 1.
    # Resultado final: Si sales del bucle sin haber encontrado el target, retorna False.
# Este enfoque garantiza una complejidad de tiempo de O(log(m * n)), lo cual es adecuado para las restricciones dadas.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Example 1:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Output: true
print(Solution().searchMatrix(matrix, target))

# Example 2:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
# Output: false
print(Solution().searchMatrix(matrix, target))
