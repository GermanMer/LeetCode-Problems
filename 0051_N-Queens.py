#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

#Example 1:
#Input: n = 4
#Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

#Example 2:
#Input: n = 1
#Output: [["Q"]]

#Constraints:
#1 <= n <= 9

# Para resolver el problema de las n-reinas, necesitamos encontrar todas las formas posibles de colocar n reinas en un tablero de n x n de manera que ninguna de ellas se ataque entre sí. Una reina puede atacar cualquier pieza que esté en la misma fila, columna o diagonal. Por lo tanto, nuestro objetivo es asegurarnos de que ninguna reina esté en la misma fila, columna o diagonal que otra.
# Enfoque: Utilizaremos un enfoque de backtracking (retroceso) para explorar todas las posibles ubicaciones de las reinas en el tablero. A continuación se describen los pasos principales del algoritmo:
    # Configuración del Backtracking: Usaremos backtracking para probar todas las posibles ubicaciones de las reinas en el tablero. Para hacerlo de manera eficiente, mantendremos tres conjuntos para seguir el rastro de las columnas y diagonales que están ocupadas por reinas.
    # Seguimiento de Ataques:
        # cols: Conjunto que mantiene las columnas donde ya hay reinas.
        # diagonals1: Conjunto que mantiene los valores de las diagonales row - col (diagonales que van de la esquina superior izquierda a la esquina inferior derecha).
        # diagonals2: Conjunto que mantiene los valores de las diagonales row + col (diagonales que van de la esquina superior derecha a la esquina inferior izquierda).
    # Función Recursiva: Usaremos una función recursiva para colocar reinas fila por fila. En cada fila, intentamos colocar una reina en cada columna y verificamos si es seguro hacerlo (es decir, si la columna y ambas diagonales no están atacadas).
    # Construcción de Soluciones: Una vez que encontramos una configuración válida, construimos la configuración del tablero y la almacenamos.

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        return results

#Example 1:
n = 4
#Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(Solution().solveNQueens(n))

#Example 2:
n = 1
#Output: [["Q"]]
print(Solution().solveNQueens(n))

# Explicación del Código:
    # Definición de la Función backtrack: Esta función se encarga de intentar colocar una reina en cada columna de la fila actual y verificar si es una posición válida. Si se coloca una reina, se actualizan los conjuntos de columnas y diagonales ocupadas y se realiza una llamada recursiva para la siguiente fila.
    # Agregar y Quitar Reinas: Si colocamos una reina en una posición válida, se actualizan los conjuntos correspondientes y se hace la llamada recursiva. Después de regresar de la llamada recursiva, se eliminan las actualizaciones para probar otras posibles ubicaciones (retroceso).
    # Construcción del Tablero: Una vez que se encuentra una solución completa (cuando row es igual a n), se construye la representación del tablero en formato de lista de cadenas y se agrega a los resultados.
    # Inicialización y Llamada Inicial: Inicializamos los conjuntos y la lista de soluciones y llamamos a la función backtrack para comenzar a resolver el problema desde la primera fila.
