#Write a program to solve a Sudoku puzzle by filling the empty cells.

#A sudoku solution must satisfy all of the following rules:
    #Each of the digits 1-9 must occur exactly once in each row.
    #Each of the digits 1-9 must occur exactly once in each column.
    #Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    #The '.' character indicates empty cells.

#Example 1:
#Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
#Explanation: The input board is shown above and the only valid solution is shown below:

#Constraints:
#board.length == 9
#board[i].length == 9
#board[i][j] is a digit or '.'.
#It is guaranteed that the input board has only one solution.

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Resuelve el rompecabezas de Sudoku modificando el tablero en su lugar.
        """

        def is_valid(board, row, col, num):
            """
            Verifica si es válido colocar 'num' en la posición (row, col).
            """
            # Verifica la fila
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Verifica la columna
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Verifica el sub-cuadro 3x3
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        def solve():
            """
            Intenta resolver el tablero de Sudoku utilizando backtracking.
            """
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        # Intenta colocar un número del 1 al 9
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                # Llama recursivamente a solve para intentar completar el tablero
                                if solve():
                                    return True
                                # Si no fue posible, deshace la asignación
                                board[i][j] = '.'
                        # Si ningún número es válido, retrocede
                        return False
            # Si no quedan celdas vacías, el tablero está resuelto
            return True

        solve()

# Ejemplo de uso
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solver = Solution()
solver.solveSudoku(board)

# Imprime el tablero resuelto
for row in board:
    print(row)
