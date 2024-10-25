# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1

# Constraints:
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

# Enfoque de Programación Dinámica:
    # Inicializar la Matriz: Creamos una matriz dp donde dp[i][j] representa el número de maneras de llegar a la celda (i, j).
    # Condiciones Iniciales:
        # Si la celda de inicio obstacleGrid[0][0] es un obstáculo (1), entonces no hay forma de comenzar, y el resultado es 0.
        # Si no hay obstáculos, inicializamos dp[0][0] a 1.
    # Llenar la Matriz:
        # Para cada celda (i, j), si no hay un obstáculo en esa celda, el número de maneras de llegar a ella es la suma de las maneras de llegar desde la celda de arriba y la celda de la izquierda.
        # Si hay un obstáculo, simplemente mantenemos dp[i][j] como 0.
    # Resultado: El valor en dp[m-1][n-1] nos dará el número total de caminos únicos al final.

# Los enfoques combinatorio y de recursión con memorización no son recomendables porque presentan ciertas limitaciones y complicaciones en este caso con obstáculos.

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Si la celda de inicio o la celda final es un obstáculo
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Crear la matriz dp
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Hay una forma de estar en la celda inicial

        # Llenar la primera fila
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        # Llenar la primera columna
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        # Llenar el resto de la matriz
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # Solo si no hay un obstáculo
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]  # Número de caminos únicos al final

# Example 1:
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
print(Solution().uniquePathsWithObstacles(obstacleGrid))

# Example 2:
obstacleGrid = [[0,1],[0,0]]
# Output: 1
print(Solution().uniquePathsWithObstacles(obstacleGrid))
