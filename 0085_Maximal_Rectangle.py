# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:
# Input: matrix =
# [["1","0","1","0","0"],
# ["1","0","1","1","1"],
# ["1","1","1","1","1"],
# ["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Example 3:
# Input: matrix = [["1"]]
# Output: 1

#  Constraints:
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

# Para resolver el problema se puede utilizar una técnica similar a la resolución del problema anterior de encontrar el área máxima de un histograma, tratando cada fila de la matriz como la base de un histograma, donde el valor de cada celda en la fila (si es un "1") indica la altura de la barra del histograma.

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0  # Si la matriz está vacía, no hay rectángulo, por lo que el área es 0

        # Convertir las cadenas de "1" y "0" a enteros para hacer operaciones matemáticas más fáciles
        matrix = [[int(cell) for cell in row] for row in matrix]

        # Número de filas y columnas de la matriz
        rows = len(matrix)
        cols = len(matrix[0])

        # Inicializamos un array de alturas para representar el histograma
        heights = [0] * cols
        max_area = 0  # Inicializamos la variable que almacenará el área máxima encontrada

        # Recorrer cada fila de la matriz
        for i in range(rows):
            for j in range(cols):
                # Si encontramos un '1', acumulamos la altura del histograma
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    # Si encontramos un '0', la altura del histograma se reinicia a 0
                    heights[j] = 0

            # Una vez que hemos actualizado las alturas para la fila actual,
            # calculamos el área máxima posible utilizando el histograma en heights
            max_area = max(max_area, self.max_histogram_area(heights))

        return max_area

    # Función para calcular el área máxima en un histograma utilizando una pila
    def max_histogram_area(self, heights: List[int]) -> int:
        stack = []  # Pila para almacenar los índices de las barras del histograma
        max_area = 0  # Área máxima en el histograma

        # Recorrer todas las barras del histograma
        for i in range(len(heights)):
            # Mientras la pila no esté vacía y la barra actual sea más baja que la barra
            # en el índice superior de la pila, calculamos el área del rectángulo
            # usando la barra en el tope de la pila como la altura.
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Altura de la barra en el tope de la pila
                w = i if not stack else i - stack[-1] - 1  # Ancho del rectángulo
                max_area = max(max_area, h * w)

            # Empujamos el índice actual en la pila
            stack.append(i)

        # Al finalizar, hay que procesar las barras restantes en la pila
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)

        return max_area

# Example 1:
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
print(Solution().maximalRectangle(matrix))

# Example 2:
matrix = [["0"]]
# Output: 0
print(Solution().maximalRectangle(matrix))

# Example 3:
matrix = [["1"]]
# Output: 1
print(Solution().maximalRectangle(matrix))
