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

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int):
            if row == n:
                # Se ha encontrado una solución válida, añádela a los resultados
                board = []
                for r in range(n):
                    board.append("".join(["Q" if c == solution[r] else "." for c in range(n)]))
                results.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                # Colocar la reina
                solution[row] = col
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Recur para colocar la siguiente reina
                backtrack(row + 1)

                # Quitar la reina y retroceder
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        results = []
        solution = [-1] * n  # Lista para almacenar el índice de columna de las reinas en cada fila
        cols = set()  # Columnas donde se colocan las reinas
        diagonals1 = set()  # Diagonales de arriba a la izquierda a abajo a la derecha
        diagonals2 = set()  # Diagonales de arriba a la derecha a abajo a la izquierda

        backtrack(0)
        return len(results)

#Example 1:
n = 4
#Output: 2
print(Solution().totalNQueens(n))

#Example 2:
n = 1
#Output: 1
print(Solution().totalNQueens(n))
