#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return the number of distinct solutions to the n-queens puzzle.

#Example 1:
#Input: n = 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

#Example 2:
#Input: n = 1
#Output: 1

#Constraints:
#1 <= n <= 9

# Para resolver el problema de contar el número de soluciones distintas para el problema de las n-reinas, podemos usar un enfoque similar al que usamos para encontrar todas las soluciones, pero en lugar de almacenar todas las soluciones, simplemente contaremos cuántas soluciones válidas encontramos.
# Eficiencia en Memoria: Esta versión optimizada usa menos memoria ya que no guarda todas las soluciones, solo cuenta cuántas hay. Esto es especialmente importante cuando n es grande.

from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int):
            if row == n:
                # Se ha encontrado una solución válida
                nonlocal count
                count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                # Colocar la reina
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Recur para colocar la siguiente reina
                backtrack(row + 1)

                # Quitar la reina y retroceder
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        count = 0
        cols = set()  # Columnas donde se colocan las reinas
        diagonals1 = set()  # Diagonales de arriba a la izquierda a abajo a la derecha
        diagonals2 = set()  # Diagonales de arriba a la derecha a abajo a la izquierda

        backtrack(0)
        return count

#Example 1:
n = 4
#Output: 2
print(Solution().totalNQueens(n))

#Example 2:
n = 1
#Output: 1
print(Solution().totalNQueens(n))
