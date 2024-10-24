# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Constraints:
# 1 <= m, n <= 100

# Enfoque de Recursión con Memorización:
# Calculas el número de caminos desde una posición dada y almacenas los resultados para evitar cálculos repetidos.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def count_paths(x, y):
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            if (x, y) in memo:
                return memo[(x, y)]

            # Sumar las maneras de llegar desde arriba y desde la izquierda
            memo[(x, y)] = count_paths(x - 1, y) + count_paths(x, y - 1)
            return memo[(x, y)]

        return count_paths(m - 1, n - 1)

# Example 1:
m = 3
n = 7
# Output: 28
print(Solution().uniquePaths(m, n))

# Example 2:
m = 3
n = 2
# Output: 3
print(Solution().uniquePaths(m, n))
