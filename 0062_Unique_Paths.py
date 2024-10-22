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

# Enfoque Combinatorio:
# El robot tiene que realizar un total de m − 1 movimientos hacia abajo y n − 1 movimientos hacia la derecha para llegar a la esquina inferior derecha. En total, necesitará hacer (m − 1) + (n − 1) = m + n − 2 movimientos.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial

        def combinatorio(n, k):
            return factorial(n) // (factorial(k) * factorial(n - k))

        return combinatorio(m + n - 2, m - 1)

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
