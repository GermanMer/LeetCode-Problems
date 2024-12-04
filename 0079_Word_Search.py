# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]
# ], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Función auxiliar de búsqueda en profundidad (DFS, por sus siglas en inglés).
        # DFS es un algoritmo que se utiliza para explorar todos los nodos y aristas de un grafo o estructura similar (como un árbol o, en este caso, una cuadrícula). Funciona explorando tan profundamente como sea posible a lo largo de cada rama antes de retroceder.
        def dfs(board, word, i, j, index):
            # Comprobar si se ha encontrado la palabra
            if index == len(word):
                return True

            # Comprobar límites y coincidencias
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False

            # Marcar la celda como visitada
            temp = board[i][j]
            board[i][j] = '#'  # Marcar como visitada

            # Explorar las celdas adyacentes
            found = (dfs(board, word, i + 1, j, index + 1) or  # Abajo
                dfs(board, word, i - 1, j, index + 1) or  # Arriba
                dfs(board, word, i, j + 1, index + 1) or  # Derecha
                dfs(board, word, i, j - 1, index + 1))    # Izquierda

            # Desmarcar la celda
            board[i][j] = temp  # Restaurar la celda

            return found


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Solo comenzar desde coincidencias
                    if dfs(board, word, i, j, 0):
                        return True
        return False

# Example 1:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# Output: true
print(Solution().exist(board, word))

# Example 2:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
# Output: true
print(Solution().exist(board, word))

# Example 3:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
# Output: false
print(Solution().exist(board, word))
