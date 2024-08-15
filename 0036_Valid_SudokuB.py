#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

#Example 1:
#Input: board =
#[["5","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: true

#Example 2:
#Input: board =
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

#Constraints:
#board.length == 9
#board[i].length == 9
#board[i][j] is a digit 1-9 or '.'.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Usamos conjuntos para llevar el seguimiento de los números vistos en filas, columnas y sub-cajas
        filas = [set() for _ in range(9)]
        columnas = [set() for _ in range(9)]
        sub_cajas = [set() for _ in range(9)]

        # Recorremos cada celda del tablero
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue  # Si la celda está vacía, continuamos con la siguiente iteración

                # Verificamos si el número ya ha sido visto en la fila actual
                if num in filas[r]:
                    return False
                filas[r].add(num)  # Agregamos el número al conjunto de la fila

                # Verificamos si el número ya ha sido visto en la columna actual
                if num in columnas[c]:
                    return False
                columnas[c].add(num)  # Agregamos el número al conjunto de la columna

                # Calculamos el índice de la sub-caja de 3x3
                indice_sub_caja = (r // 3) * 3 + (c // 3)

                # Verificamos si el número ya ha sido visto en la sub-caja actual
                if num in sub_cajas[indice_sub_caja]:
                    return False
                sub_cajas[indice_sub_caja].add(num)  # Agregamos el número al conjunto de la sub-caja

        # Si no hemos encontrado ningún duplicado, el tablero es válido
        return True

#Example 1:
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: true
print(Solution().isValidSudoku(board))

#Example 2:
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: false
print(Solution().isValidSudoku(board))
