# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# Enfoque General: Para resolver el problema de recorrer una matriz en orden espiral seguiremos un enfoque que consiste en mantener un control de los límites de la matriz que se debe explorar.
    # Definir los límites: Necesitas definir los límites superior, inferior, izquierdo y derecho de la parte de la matriz que aún no has recorrido. Estos límites te ayudarán a saber cuándo cambiar de dirección.
    # Recorrer en espiral:
        # Empieza desde el borde superior y avanza hacia la derecha.
        # Luego, recorre el borde derecho de arriba hacia abajo.
        # Después, recorre el borde inferior de derecha a izquierda.
        # Finalmente, recorre el borde izquierdo de abajo hacia arriba.
    # Ajusta los límites después de cada paso para moverte hacia el siguiente "anillo" espiral.
    # Detenerse cuando los límites se cruzan: Deja de recorrer cuando el límite superior sea mayor que el inferior o el límite izquierdo sea mayor que el derecho.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        # Dimensiones de la matrix
        m = len(matrix) # Número de filas (alto de la matriz)
        n = len(matrix[0]) # Número de columnas (ancho de la matriz)

        # Límites iniciales
        top = 0
        right = n - 1
        bottom = m - 1
        left = 0

        # Bucle para recorrer el espiral
        while top <= bottom and left <= right:

            # Recorrer de izquierda a derecha en el borde superior
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Mover el límite superior hacia abajo

            # Recorrer de arriba hacia abajo en el borde derecho
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 # Mover el límite derecho hacia la izquierda

            if top <= bottom: # Si aún no se ha cruzado con top
                # Recorrer de derecha a izquierda en el borde inferior
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Mover el límite inferior hacia arriba

            if left <= right: # Si aún no se ha cruzado con right
                # Recorrer de abajo hacia arriba en el borde izquierdo
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Mover el límite izquierdo hacia la derecha

        return result

#Example 1:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
print(Solution().spiralOrder(matrix))

#Example 2:
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(Solution().spiralOrder(matrix))
